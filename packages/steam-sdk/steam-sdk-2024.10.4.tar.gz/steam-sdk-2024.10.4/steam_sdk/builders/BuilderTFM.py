import numpy as np
import pandas as pd
import os
import copy
from pathlib import Path
from dataclasses import asdict
from scipy.interpolate import RegularGridInterpolator
from scipy.interpolate import interp1d
from scipy.signal import find_peaks

from steam_sdk.data.DataTFM import General, Turns, HalfTurns, Strands, PC, Options, IFCC, ISCC, ED, Wedge, CB, CPS, AlRing, BS, Shorts
from steam_sdk.data.DataTFM import lookupModelDataToTFMHalfTurns, lookupModelDataToTFMStrands
from steam_sdk.data.DataModelCircuit import Component
from steam_sdk.parsers.ParserXYCE import ParserXYCE
from steammaterials.STEAM_materials import STEAM_materials
import matplotlib.pyplot as plt

class BuilderTFM:
    """
        **Class for Generating TFM Models**

        `BuilderTFM` is designed to work with the `Options` data class, which contains flags for all the effects acting on the magnets.
        Each new effect must be added as both:
        - A new data class in `DataTFM`.
        - A new flag in the `Options` data class.

        Non-Conductor effects (e.g., Wedge, CB, CPS, AlRing, BS) should be added as flags in the upper section of the `Options` data class, before the flags for conductor losses.

        **Key Rules for Implementation:**

        1. Each effect must have a dedicated flag in the `Options` data class and a corresponding data class in `DataTFM`, named after the effect.
        2. Flags for Non-Conductor losses must always be positioned above the flags for Conductor Losses in the `Options` data class.

        **Additional Requirements for Non-Conductor Effects:**

        For each Non-Conductor effect, multiple `.csv` files are required to calculate its contribution. A COMSOL MultiPhysics model is needed to evaluate eddy currents in the metallic component. From each model, the following `.csv` files must be exported:

        1. Induced current data.
        2. Power loss data.
        3. Magnetic field data for each strand position.
"""



    def __init__(self, builder_LEDET= None, flag_build: bool = True,
                  output_path: str = None, local_library_path: str = None, TFM_inputs=None, magnet_data=None,
                 circuit_data=None, verbose: bool = True ):
        """
            Object is initialized by defining the TFM variable structure and default parameter descriptions, starting from
            the `magnet_name` and the `builder_LEDET` model. The class can also calculate various passive effects depending on the flag values.

            :param magnet_name: Name of the analyzed magnet.
            :param builder_LEDET: `builderLEDET` object corresponding to the magnet.
            :param flag_build: Defines whether the model needs to be built.
            :param output_path: Path to save the generated `.lib` file.
            :param TFM_inputs: `TFMClass` from `DataModelCircuit.py` in `steam_sdk.data`, includes:

                - **flag_PC**, **flag_ISCC**, **flag_IFCC**, **flag_ED**, **flag_Wedge**, **flag_CB**, **flag_BS**: Flag effects.
                - **M_CB_wedge**: Value of the mutual coupling between ColdBore and Wedge.
                - **T**: Simulation temperature.

            :param Magnet_data: `Magnet` class from `DataModelCircuit.py` in `steam_sdk.data`, includes:

                - **name**: Magnet name.
                - **L_mag**: Total inductance of the magnet.
                - **C_ground**: Total capacitance to ground of the magnet circuit.
                - **field_interp_value**: If not `None`, specifies the parameter value for which to find `f_mag`,
                  differentiating field files extracted from COMSOL by a parameter other than temperature.
                  If `None`, the `field_interp_value` used is the temperature `T`.
        """

        self.verbose = verbose
        self.General = General()
        self.Turns = Turns()
        self.HalfTurns = HalfTurns()
        self.Strands = Strands()
        self.Options = Options()
        self.PC = PC()
        self.IFCC = IFCC()
        self.ISCC = ISCC()
        self.ED = ED()
        self.Wedge = Wedge()
        self.CB = CB()
        self.CPS = CPS()
        self.AlRing = AlRing()
        self.BS = BS()
        self.Shorts = Shorts()
        self.print_nodes = []

        # TODO: HardCoded values -> tau constant AlRing
        self.General.apertures = 2
        self.effs_cond = ['PC','ISCC','IFCC','ED']
        frequency = np.logspace(0, 6, 120 + 1)
        self.frequency = frequency
        self.mu0 = 4 * np.pi / 1e7

        if flag_build:
            if not builder_LEDET or not magnet_data.name:
                 raise Exception('Cannot build model without providing BuilderLEDET object with Inputs dataclass and magnet_name')

            self.magnet_name = magnet_data.name
            self.magnet_circuit_name = magnet_data.circuit_name
            # Set-up magnet components and validate some inputs
            for keyMagnetData, value in magnet_data.__dict__.items():
                if 'magnet_' in keyMagnetData and keyMagnetData != 'magnet_Couplings':
                    eff = keyMagnetData.split('_')[-1]
                    if value:
                        if eff == 'CPS':
                            if isinstance(value.rho_CPS, str):
                                if value.rho_CPS == 'SS':
                                    value.rho_CPS = self.__rhoSS_nist(TFM_inputs.temperature)
                                elif 'e-' in value.rho_CPS:
                                    value.rho_CPS = np.array([float(value.rho_CPS)])
                                else:
                                    raise Exception(f'Do not understand rho_CPS {value.rho_CPS}')
                        self.__setAttribute(self, f'{eff}', value)
            self.local_library_path = local_library_path
            self.B_nom_center = TFM_inputs.B_nom_center

            # Translate the Inputs dataclass of BuilderLEDET in a dictionary
            ledet_inputs = asdict(builder_LEDET.Inputs)
            self.ledet_inputs = ledet_inputs
            self.ledet_auxiliary = builder_LEDET.Auxiliary
            self.ledet_options = builder_LEDET.Options
            self.TFM_inputs = TFM_inputs
            self.magnet_data = magnet_data

            self.current = TFM_inputs.current
            self.temperature = TFM_inputs.temperature
            self.output_path = output_path
            self.flag_debug = TFM_inputs.flag_debug

            self.conductor_to_group = np.array(builder_LEDET.model_data.CoilWindings.conductor_to_group)


            self.__assignTurnsToSections()
            self.__translateModelDataToTFMGeneral()
            self.__translateModelDataToTFMHalfTurns()
            self.__translateModelDataToTFMStrands()
            self.__setOptions()

            self.domain = circuit_data.Analysis.analysis_type
            # Calculation of the characteristic frequency, in case the domain is transient
            if self.domain == 'transient':
                self.f_characteristic = self.__calculate_characteristic_frequency(circuit_data)
            else:
                self.f_characteristic = 0 # not needed

            if output_path is not None:
                library_name = circuit_data.Netlist[self.magnet_circuit_name].value
                self.__generate_library(output_path=output_path, library_name=library_name, verbose=self.verbose)
                self.change_coupling_parameter()

    ####################################################################################################################
    ######################################## TFM DATACLASSES ATTRIBUTE SETTING ########################################

    def __calculate_characteristic_frequency(self, circuit_data=None):
        '''
            Calculate the characteristic frequency of a circuit, approximating all have the same C and L
        '''

        netlist = circuit_data.Netlist
        n_mags = 0
        for key in netlist.keys():
            if 'x_mag' in key.casefold():
                n_mags = n_mags + 1
        self.__calculate_Inductance_Sections()
        return 1 / (n_mags * np.sqrt(self.General.L_mag * self.General.C_ground))


    def __assignTurnsToSections(self):
        '''
        This function assigns the value to turns_to_sections vector in the Turns dataclass attributes.

        This function assigns the value to turns_to_apertures vector in the Turns dataclass attributes.

        This function assigns the value to HalfTurns_to_sections vector in the HalfTurns dataclass attributes.

        turns_to_sections is a vector long as the number of turns and each element contains the id of the section to which it is assigned.

        A section is a LRC circuit inside the magnet circuit in the generated lib file
        '''
        nT = self.ledet_inputs['nT']
        n_Turns = np.sum(nT)// 2
        elPair_grouped = self.ledet_auxiliary.elPairs_GroupTogether
        elPairs_RevElOrder = self.ledet_auxiliary.elPairs_RevElOrder
        HalfTurns_to_groups = np.repeat(np.arange(len(nT)) + 1, nT)

        # the first half of elPairs_GroupTogether will be assigned to the first aperture, the second half to the second aperture
        if self.General.apertures == 2:
            idx = 0
            turns_to_apertures = np.zeros(n_Turns, dtype=int)
            for ap in range(1, 2 + 1):
                for i in range(idx, idx + len(elPair_grouped) // 2):
                    idx_group = elPair_grouped[i][0] if elPair_grouped[i][0] < elPair_grouped[i][1] else elPair_grouped[i][1]
                    idx_T = np.where(HalfTurns_to_groups == idx_group)[0]
                    turns_to_apertures[np.ix_(idx_T)] = ap
                idx = idx + len(elPair_grouped) // 2
        elif self.General.apertures==1:
            raise Exception('Inputs assume more than two apertures.')
        else:
            turns_to_apertures = np.ones((len(HalfTurns_to_groups),))
        self.__setAttribute(self.Turns, 'turns_to_apertures', turns_to_apertures)
        HalfTurns_to_apertures =  np.tile(turns_to_apertures, 2)
        self.__setAttribute(self.HalfTurns, 'HalfTurns_to_apertures', HalfTurns_to_apertures)

        if self.magnet_data.turn_to_section is not None: # If turn_to_section is not none, the turns_to_section vector is the one specified as input of the yaml file
            self.magnet_data.turn_to_section = np.array(self.magnet_data.turn_to_section).astype(int)
            n_sections = max(self.magnet_data.turn_to_section)
            for i in range(1,n_sections+1):
                if i in self.magnet_data.turn_to_section: continue
                else: raise Exception(f'Group {i} is not assigned to any turn. Please check!')
            turns_to_sections = np.array(self.magnet_data.turn_to_section).astype(int)
            ap_turns_to_sections = turns_to_sections
            HalfTurns_to_sections = np.tile(ap_turns_to_sections, 2).astype(int)
            turns_to_sections = ap_turns_to_sections

            sections_to_apertures = np.zeros((n_sections,))
            for i in range(1,n_sections+1):
                sections_to_apertures[i-1] = np.unique(turns_to_apertures[np.where(ap_turns_to_sections==i)[0]])[0]
            self.__setAttribute(self.General, 'sections_to_apertures', sections_to_apertures.astype(int))
        else:
            conductor_to_group = self.conductor_to_group
            HalfTurns_to_sections = conductor_to_group[HalfTurns_to_groups - 1]
            turns_to_sections = HalfTurns_to_sections[:int(len(HalfTurns_to_sections)/2)]  # To get turns_to_section from Halfturns_to_sections we take one element every two elements
            if self.General.apertures==2 and max(turns_to_sections)==1:  # If we have only one conductor but two apertures we set Ap1 = Section 1 and Ap2 = Section 2
                turns_to_sections = turns_to_apertures
                sections_to_apertures = np.array([1, 2]).astype(int)
                self.__setAttribute(self.General, 'sections_to_apertures', sections_to_apertures)
            else: # Else we set the first n_conductor groups in Aperture one and the 2nd n_conductor groups in Aperture 2
                turns_to_sections[np.where(turns_to_apertures == 2)[0]] += max(conductor_to_group)
                sections_to_apertures = np.array([1]*max(conductor_to_group)+[2]*max(conductor_to_group)).astype(int)
                self.__setAttribute(self.General, 'sections_to_apertures', sections_to_apertures)
            HalfTurns_to_sections = np.concatenate([turns_to_sections, turns_to_sections])
            ap_turns_to_sections = turns_to_sections

        self.__setAttribute(self.Turns, 'turns_to_sections', ap_turns_to_sections.astype(int))
        self.__setAttribute(self.HalfTurns, 'HalfTurns_to_sections', HalfTurns_to_sections.astype(int))

        #### Assign the correct electrical order to the sections
        indexTstop = np.cumsum(nT)
        indexTstop = indexTstop.tolist()
        indexTstart = [1]
        for i in range(len(nT) - 1):
            indexTstart.extend([indexTstart[i] + nT[i]])
        el_order_half_turns = [];
        for p in range(len(elPair_grouped)):
            if nT[elPair_grouped[p][0] - 1] != nT[elPair_grouped[p][1] - 1]:
                raise Exception(
                    'Pair of groups defined by the variable elPairs_GroupTogether must have the same number of half-turns.')
            for k in range(nT[elPair_grouped[p][0] - 1]):
                if elPairs_RevElOrder[p] == 0:
                    el_order_half_turns.append(indexTstart[elPair_grouped[p][0] - 1] + k);
                    el_order_half_turns.append(indexTstart[elPair_grouped[p][1] - 1] + k);
                if elPairs_RevElOrder[p] == 1:
                    el_order_half_turns.append(indexTstop[elPair_grouped[p][0] - 1] - k);
                    el_order_half_turns.append(indexTstop[elPair_grouped[p][1] - 1] - k);
        el_order_half_turns_Array = np.int_(el_order_half_turns)

        el_order_sections = np.zeros((len(el_order_half_turns_Array),))
        for i in range(1, len(HalfTurns_to_sections) + 1):
            el_order_sections[np.where(el_order_half_turns_Array == i)[0][0]] = HalfTurns_to_sections[i - 1]
        change_indices = np.diff(el_order_sections) != 0
        result = np.append(True, change_indices)
        el_order_sections = el_order_sections[result]
        self.__setAttribute(self.General, 'el_order_sections',
                            np.array(list(dict.fromkeys(el_order_sections))).astype(int))
        self.__setAttribute(self.General, 'el_order_to_apertures',
                            sections_to_apertures[np.array(list(dict.fromkeys(el_order_sections))).astype(int) - 1])


    def __translateModelDataToTFMGeneral(self):
        '''
        This function saves the appropriate BuilderLEDET Inputs dataclass values for the General dataclass attributes.

        L_mag instead is set in the function __calculate_Inductance_Sections
        '''
        self.__setAttribute(self.General, 'magnet_name', self.magnet_name)
        self.__setAttribute(self.General, 'magnet_length', self.ledet_inputs['l_magnet'])
        self.__setAttribute(self.General, 'I_magnet', self.current)
        self.__setAttribute(self.General, 'local_library_path', self.local_library_path)
        nT = self.ledet_inputs['nT']
        self.__setAttribute(self.General, 'num_HalfTurns', np.sum(nT))
        n_groups = max(self.Turns.turns_to_sections)
        self.__setAttribute(self.General, 'groups', n_groups)
        # self.__setAttribute(self.General, 'apertures', max(self.Turns.turns_to_apertures))
        C_ground = float(self.magnet_data.C_ground)
        self.__setAttribute(self.General, 'C_ground', C_ground)


    def __calculate_warm_resistance(self): # Utility function to calculate R_warm in self.General and self.HalfTurns
        '''
            Function to calculate the warm resistance, both per cable and per magnet

            It saves the R_warm_cable n the HalfTurns dataclass and the R_warm in the General dataclass
        '''

        if self.Options.flag_SC:
            # If the Magnet is in SC state, let's set by default a warm resistance of 1nOhm
            R_warm = 1e-9
            R_warm_cable = np.repeat(R_warm, self.General.num_HalfTurns)
        else:
            RRR = self.HalfTurns.RRR
            T = self.temperature
            fsc = self.Strands.fsc
            dws = self.Strands.diameter
            l = self.General.magnet_length
            I = self.General.I_magnet
            HT_to_Strands = self.HalfTurns.n_strands

            B = self.Strands.f_mag_Roxie * I
            B = B[:, 0]
            # Area of the strands
            Area_strands = (1-fsc) * np.pi * (dws/2) ** 2

            cont = 0
            A_cable = []
            B_cable = []

            # For each HalfTurns, calculates the total Area as the sum of the Areas of each strand corresponding to that HalfTurn
            # For each HalfTurns, calculates the total B as the average of the B of each strand corresponding to that HalfTurn
            for i in range(self.General.num_HalfTurns):
                n_strand_cable = HT_to_Strands[i]
                A_cable_HT = np.sum(Area_strands[cont: cont+n_strand_cable])
                B_cable_HT = np.mean(B[cont: cont+n_strand_cable])
                A_cable.append(A_cable_HT)
                B_cable.append(B_cable_HT)
                cont += n_strand_cable

            rho = self.__rhoCu_nist(T=T, RRR= np.repeat(RRR, self.General.num_HalfTurns), B=np.array(B_cable))
            # Calculates the R_warm for each HalfTurn as R_HT = rho_HT * l_mag / A_HT
            R_warm_cable = rho * l / (np.array(A_cable))
            # Calculates the total R_warm as the sum of R_warm_HT
            R_warm = np.sum(R_warm_cable)

        self.__setAttribute(self.HalfTurns, 'R_warm', R_warm_cable)
        self.__setAttribute(self.General, 'R_warm', R_warm)


    def __translateModelDataToTFMHalfTurns(self):
        '''
        This function saves the appropriate BuilderLEDET Inputs dataclass values for the HalfTurns dataclass attributes.

        The saved data are arrays with len equal to the total number of HalfTurns
        '''
        # Values that can't be directly obtained from the Inputs dataclass
        nT = self.ledet_inputs['nT']
        HalfTurns_to_groups = np.repeat(np.arange(len(nT)) + 1, nT)
        self.__setAttribute(self.HalfTurns, 'HalfTurns_to_groups', HalfTurns_to_groups)
        HalfTurns_to_conductor = self.conductor_to_group[HalfTurns_to_groups - 1]
        self.__setAttribute(self.HalfTurns, 'HalfTurns_to_conductor', HalfTurns_to_conductor)
        turns_to_conductor = HalfTurns_to_conductor[::2]
        nc = np.repeat(nT, nT)
        self.__setAttribute(self.HalfTurns, 'Nc', nc)

        # Values that can be directly obtained from the Inputs dataclass
        for keyInputData, value in self.ledet_inputs.items():
            keyTFM = lookupModelDataToTFMHalfTurns(keyInputData)
            if keyTFM in self.HalfTurns.__annotations__:
                if isinstance(value, list):
                    self.__setAttribute(self.HalfTurns, keyTFM, np.array(value))
                else:
                    self.__setAttribute(self.HalfTurns, keyTFM, value[HalfTurns_to_groups - 1])
        # Fitting value for ISCL, varying between C=1 (Ns=8) and C=1.15 (Ns=40) [-]
        # Reference: Arjan's Thesis, Chapter 4, Page 78, Equation 4.31
        C_strand = 0.0046875 * self.HalfTurns.n_strands + 0.9625
        self.__setAttribute(self.HalfTurns, 'C_strand', C_strand)


    def __translateModelDataToTFMStrands(self):
        '''
        This function saves the appropriate BuilderLEDET Inputs dataclass values for the Strands dataclass attributes.

        The saved data are arrays with len equal to the total number of Strands
        '''
        strands_to_conductor = np.repeat(self.HalfTurns.HalfTurns_to_conductor, self.HalfTurns.n_strands)
        self.__setAttribute(self.Strands, 'strands_to_conductor', strands_to_conductor)
        strands_to_sections = np.repeat(self.HalfTurns.HalfTurns_to_sections, self.HalfTurns.n_strands)
        self.__setAttribute(self.Strands, 'strands_to_sections', strands_to_sections)
        for keyLedetData, value in self.ledet_inputs.items():
            keyTFM = lookupModelDataToTFMStrands(keyLedetData)
            if keyTFM in self.Strands.__annotations__:
                repeated_value = np.repeat(value[self.HalfTurns.HalfTurns_to_groups - 1], self.HalfTurns.n_strands)
                self.__setAttribute(self.Strands, keyTFM, repeated_value)
        self.__calculate_field_contributions()


    def __setOptions(self):
        '''
        This function sets to the Option DataClass the flags to know which effects should be included in the magnet model

        :attribute flag_PC: if True includes the Persistent Current effect

        :attribute flag_IFCC: if True includes the Inter Filament Coupling Current effect

        :attribute flag_ISCC: if True includes the Inter Strands Coupling Current effect

        :attribute flag_Wedge: if True includes the Wedge effect

        :attribute flag_CB: if True includes the Cold Bore effect

        :attribute flag_ED: if True includes the Eddy Currents effect in the Copper Sheath

        :attribute flag_BS: if True includes the BeamScreen effect in the Copper Sheath

        :attribute flag_SC: set to True depending on the T (indicates if a magnet is in Superconducting state)
        '''
        if self.temperature <  min(self.ledet_inputs['Tc0_NbTi_ht_inGroup']):
            flag_SC = True
        else:
            flag_SC = False

        self.__setAttribute(self.Options, 'flag_SC', flag_SC)
        self.__calculate_warm_resistance()

        effects = {}
        self.effs_notCond = []
        for keyTFMData, value in self.TFM_inputs.__dict__.items():
            if keyTFMData.startswith('flag') and keyTFMData != 'flag_debug':
                if type(value) != bool and type(value) != int:
                    value = False
                self.__setAttribute(self.Options, keyTFMData, value)

                # Saving in a Dictionary the effects names and the flag values
                eff = keyTFMData.split('_')[-1]
                effects[eff] = value
                if eff not in self.effs_cond:
                    self.effs_notCond.append(eff)
        self.effects = effects


    def __calculate_field_contributions(self):  # Utility function to calculate f_mag in __translateModelDataToTFMStrands
        '''
        Calculates the field in each filament of the MB magnet.

        It saves in the Strands dataclass vectors of shape [len(freq), n_strands]

        : f_mag, f_mag_X and f_mag_Y taken from Roxie

        : f_mag, f_mag_X and f_mag_Y taken from the magnet Comsol Model with no effects included
        '''

        local_library_path = os.path.join(Path(self.General.local_library_path).resolve(), 'TFM_input')
        name = self.General.magnet_name
        mapping = np.vectorize(lambda t: complex(t.replace('i', 'j')))

        # Taking the excel file containing the field values of the Comsol Model without any effect
        full_file_Comsol = Path(os.path.join(local_library_path, f'Field_Map_{name}.csv')).resolve()
        df_Comsol = pd.read_csv(full_file_Comsol, header=None, dtype=str, na_filter=False)
        # Extracting the frequency values from the file
        frequency = np.array(df_Comsol.iloc[1, 2::2]).astype(float)
        self.frequency = frequency

        f_mag_Roxie, f_mag_X_Roxie, f_mag_Y_Roxie = self.__retrieve_field_contributions_Roxie()

        # Transforming the values in the files in the format (Re + i*Im) to  (Re + j*Im) -> correct complex format for Python
        df_Comsol = mapping(df_Comsol.values[2:, 2:]).T
        f_mag_X_Comsol = np.real(df_Comsol[::2, :])
        f_mag_Y_Comsol = np.real(df_Comsol[1::2, :])
        f_mag_Comsol = np.real(np.sqrt(df_Comsol[::2, :] * np.conjugate(df_Comsol[::2, :]) + df_Comsol[1::2, :] * np.conjugate(df_Comsol[1::2, :])))

        e_field = []
        self.Strands.strands_to_apertures = np.zeros((f_mag_Comsol.shape[1],))
        for ap in range(1,self.General.apertures+1):
            idx_sec = np.where(self.General.sections_to_apertures == ap)[0]
            idx_s = []
            for n in idx_sec:
                idx_s.append(np.where(self.Strands.strands_to_sections==n+1)[0])
            idx_s = [item for row in idx_s for item in row]
            e_field.append([len(np.where(np.sign(f_mag_Y_Roxie[0,idx_s])-np.sign(f_mag_Y_Comsol[0,idx_s])==0)[0])])
            self.Strands.strands_to_apertures[idx_s] = ap
        if len(e_field)>1:
            if e_field[0]>e_field[1]:
                self.General.COMSOL_ap = 1
            else:
                self.General.COMSOL_ap = 2
        else:
            self.General.COMSOL_ap = 1

        self.__setAttribute(self.Strands, 'f_mag_X_Roxie', f_mag_X_Roxie)
        self.__setAttribute(self.Strands, 'f_mag_Y_Roxie', f_mag_Y_Roxie)
        self.__setAttribute(self.Strands, 'f_mag_Roxie', f_mag_Roxie)

        self.__setAttribute(self.Strands, 'f_mag_X_Comsol', f_mag_X_Comsol)
        self.__setAttribute(self.Strands, 'f_mag_Y_Comsol', f_mag_Y_Comsol)
        self.__setAttribute(self.Strands, 'f_mag_Comsol', f_mag_Comsol)


    ####################################################################################################################
    ############################################ FUNCTIONS TO READ AND ASSIGN F_MAG #####################################
    def __read_COMSOL_field_file(self, Effect: str = None, field_int_value: float = None) -> np.ndarray:
        '''
         Calculates the diff_field in each filament due to the given effect as the mutual difference between the result of the
         '__retrieve_field_contributions_COMSOL'function and the field obtained from the Comsol simulation w/o effects.
         Then returns the field in each filament as the sum of the field from Roxie and the diff_field

         :param Effect: str that indicates the corresponding Not Conductor Loss effect -> Wedge or CB or BS or CPS or AlRing
        '''
        if Effect is not None:
            f_mag_X_Roxie = self.Strands.f_mag_X_Roxie
            f_mag_Y_Roxie = self.Strands.f_mag_Y_Roxie
            f_mag_Comsol = self.Strands.f_mag_Comsol
            f_mag_X_Comsol = self.Strands.f_mag_X_Comsol
            f_mag_Y_Comsol = self.Strands.f_mag_Y_Comsol

            fMag, fMag_X, fMag_Y = self.__retrieve_field_contributions_COMSOL(Effect=Effect, field_int_value=field_int_value)

            f_X_diff = fMag_X  - f_mag_X_Comsol
            f_Y_diff = fMag_Y  - f_mag_Y_Comsol

            idx_s = np.where(self.Strands.strands_to_apertures==self.General.COMSOL_ap)[0]
            if np.any(np.isnan(f_Y_diff[:,idx_s])): raise Exception('Error in field calculation.')
            f_Y = f_mag_Y_Roxie + f_Y_diff
            f_X = f_mag_X_Roxie + f_X_diff

            # # Fill up other aperture if not provided from COMSOL
            if (np.count_nonzero(np.isnan(f_Y_diff[0, :])) == np.count_nonzero(np.isnan(f_X_diff[0, :]))):
                if int(np.count_nonzero(np.isnan(f_Y_diff[0, :]))) == int(f_Y_diff.shape[1] / 2):
                    idx_val1 = np.where(np.isnan(f_Y_diff[0, :]))[0][0]
                    n_sections = int(len(f_Y_diff[0, :]) / idx_val1)

                    for j in range(n_sections):
                        if j % 2: continue
                        idx_start = int(len(f_Y_diff[0, :]) - (j + 1) * idx_val1)
                        idx_end = int(len(f_Y_diff[0, :]) - (j) * idx_val1)
                        idx_c_start = int(j * idx_val1)
                        idx_c_end = int((j + 1) * idx_val1)
                        f_X[:, idx_start:idx_end] = f_X[:, idx_c_start:idx_c_end]
                        f_Y[:, idx_start:idx_end] = -1*f_Y[:, idx_c_start:idx_c_end]

            f_mag = np.sqrt(f_X ** 2 + f_Y ** 2)
            return f_mag, f_X, f_Y


    def __retrieve_field_contributions_COMSOL(self, Effect: str = None, field_int_value: float = None) -> np.ndarray:
        '''
        Extracts the magnetic field data for each filament of the MB magnet from Excel files corresponding to a specific
        Comsol Model that includes a given effect.
        Multiple files exist for each effect, with each file resulting from a simulation using a different value of a
        particular parameter (usually temperature, T).

        To select the most accurate data, the function performs an interpolation between the desired value of the parameter
        and the data from the four closest simulation values saved in the Excel files.

        :param Effect: str indicating the specific Not Conductor Loss effect (either "Wedge" or "CB").

        :return f_mag: field in each filament for a magnet that includes the specified effect.
        :return f_mag_X: field along the X-axis in each filament for a magnet that includes the specified effect.
        :return f_mag_Y: field along the Y-axis in each filament for a magnet that includes the specified effect.
        '''

        local_library_path = os.path.join(Path(self.General.local_library_path).resolve(), 'TFM_input')
        frequency = self.frequency

        Param = []
        files_Field = []
        df_array_X = []
        df_array_Y = []
        df_array_Mag = []

        # value is the desired parameter for which we want to find accurate f_mag, f_mag_X, f_mag_Y
        # usually it is the T of the simulation, if it is not it can be specified in field_interp_value
        if field_int_value:
            value = field_int_value
        else:
            value = self.temperature

        # Loop to extract all the possible parameters values for the Comsol model with effect that are presents in the excel files
        for dir in os.listdir(local_library_path):
            if dir.startswith('Field_Map'):
                if Effect in dir:
                    parameter = dir.replace('.csv','').split('_')[-1]
                    Param.append(float(parameter)) # Saving the parameter values
                    files_Field.append(dir) # Saving the file directory

        Param = np.array(Param)
        files_Field = np.array(files_Field)

        if float(value) in Param: # If there is one file performed with parameter = value no need for the interpolation
            closest_Param = np.array([value]) # Taking just the value as closest parameter
        elif(value < Param.min() or value > Param.max()):# If the value is out of bounds -> error
            raise Exception('Error: Parameter out of range')
        else:
            closest_indices = np.argsort(np.abs(Param - value))[:4] # Otherwise taking the 4 closest values of the excel files
            closest_Param = Param[closest_indices]

        for i in range(len(closest_Param)): # Reading the files of the closest parameter simulations
            file = os.path.join(local_library_path, files_Field[i])
            with pd.option_context('future.no_silent_downcasting', True):
                df_COMSOL = pd.read_csv(file, header=None, dtype=str, na_filter=False).replace({'': 0})
                df_COMSOL = df_COMSOL.loc[:, (df_COMSOL != 0).any(axis=0)]
            mapping = np.vectorize(lambda t: complex(t.replace('i', 'j')))
            df_COMSOL = mapping(df_COMSOL.values[2:, 2:]).T
            # df_X = np.real(df_COMSOL[::2, :] * np.conjugate(df_COMSOL[::2, :]))
            # df_Y = np.real(df_COMSOL[1::2, :] * np.conjugate(df_COMSOL[1::2, :]))
            df_X = np.real(df_COMSOL[::2, :])
            df_Y = np.real(df_COMSOL[1::2, :])
            df_array_X.append(df_X)
            df_array_Y.append(df_Y)

        order = np.argsort(closest_Param)
        closest_Param = closest_Param[order]
        df_array_X = np.array(df_array_X)
        df_array_X = df_array_X[order]
        df_array_Y = np.array(df_array_Y)
        df_array_Y = df_array_Y[order]

        if len(closest_Param) != 1: # If there are 4 closest parameter -> interpolation to find f_mag_X and f_mag_Y
            interp_X = RegularGridInterpolator((closest_Param, frequency), df_array_X)
            new_points_X = (np.array([value]), frequency) # value = Parameter to __interpolate for = input
            f_mag_X = interp_X(new_points_X)

            interp_Y = RegularGridInterpolator((closest_Param, frequency), df_array_Y)
            new_points_Y = (np.array([value]), frequency)
            f_mag_Y = interp_Y(new_points_Y)
        else: # If there is only 1 closest parameter -> excel file with parameter = desired value, just take f_mag_X and f_mag_Y from that file
            f_mag_X = df_array_X[0, :, :]
            f_mag_Y = df_array_Y[0, :, :]

        f_mag = np.real(np.sqrt(df_COMSOL[::2, :] * np.conjugate(df_COMSOL[::2, :]) + df_COMSOL[1::2, :] * np.conjugate(df_COMSOL[1::2, :])))
        # f_mag_X = np.sqrt(f_mag_X)
        # f_mag_Y = np.sqrt(f_mag_Y)
        return f_mag, f_mag_X, f_mag_Y


    def __retrieve_field_contributions_Roxie(self) -> np.ndarray:
        '''
        Extracts the magnetic field data for each filament of the corresponding magnet fstarting from the Magnetic field
        taken from the LEDET class attributes

        :return f_mag: field in each filament for the magnet w/o effects
        :return f_mag_X: field along the X-axis in each filament for for the magnet w/o effects
        :return f_mag_Y: field along the Y-axis in each filament for the magnet w/o effects
        '''

        Bx = self.ledet_auxiliary.Bx
        By = self.ledet_auxiliary.By
        Iref = self.ledet_options.Iref

        f_mag_X = Bx / Iref
        f_mag_Y = By / Iref
        B_E = np.sqrt(Bx ** 2 + By ** 2)

        f_mag = np.sqrt(f_mag_X ** 2 + f_mag_Y ** 2)
        peakB_superPos = np.max(f_mag * Iref)
        peakB_real = np.max(B_E)
        f_peakReal_Superposition = peakB_real / peakB_superPos

        fMag_X = f_mag_X * f_peakReal_Superposition
        fMag_Y = f_mag_Y * f_peakReal_Superposition

        frequency = self.frequency
        fMag_X = np.repeat(fMag_X[:, np.newaxis], len(frequency), axis=1).T
        fMag_Y = np.repeat(fMag_Y[:, np.newaxis], len(frequency), axis=1).T
        f_mag = np.repeat(f_mag[:, np.newaxis], len(frequency), axis=1).T

        return f_mag, fMag_X, fMag_Y


    ###################################################################################################################
    ############################################### LIBRARY GENERATION ###############################################
    def __generate_library(self, output_path: str, library_name: str, verbose: bool = False):
        '''
        This function generates a suitable lib file for the magnet simulation in XYCE.

        It follows this structure:

         - Calculation of the magnet inductance values using the 'calculate_Inductance_Turn' function.

         - Initialization of the magnet circuit through the '__generate_magnet_circuit_library' function.

         - Setting up the '.FUNC' parameter for each effect using the '__generate_function_library' function.

         - Defining the circuit parameters for each effect and each loop via the '__generate_loop_library' function.

         - Establishing the mutual coupling between each effect with the '__generate_coupling_library' function.

         - Computing the mutual coupling between the inductance of different loops through the 'calculate_MutualInductance_Turns' function.

         :param output_path: directory where the lib file must be saved
        '''
        self.__setAttribute(self.General, 'lib_path', output_path)
        # The lib file is build using a Dictionary of components
        Netlist = {}
        apertures = self.General.apertures
        groups = self.General.groups
        sections_to_apertures = self.General.sections_to_apertures
        # These nodes are the ones used in the circuit yaml file as magnet nodes
        Nodes = ['EE_AP1_IN', 'EE_AP_MID', 'EE_AP2_OUT', '1_GND']

        # Comments initialization
        Comm_newline = Component(type='comment', nodes=[], value=' ')  # Introduces an empty line in the file
        Netlist['Comment_newline_b_Magnet'] = Comm_newline

        Comm = Component(type='comment', nodes=[], value='* Each section has a C_GND and a V_tap, R_warm and L in series')
        Netlist['Comm_func3'] = Comm
        Comm = Component(type='comment', nodes=[], value='* The suffix of each element have the format _{aperture}_{group}')
        Netlist['Comm_func4'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each capacitance is calculated as C_ground /(tot_num_apertures * tot_num_groups)')
        Netlist['Comm_func5'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each V_tap = 0 since it is just used to access the current in that group')
        Netlist['Comm_func6'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each R_warm is calculated as R_warm_tot / (tot_num_apertures * tot_num_groups)')
        Netlist['Comm_func7'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each L value is taken from the the Inductance Matrix in BuilderLEDET, according to the contribute of the turns associated to that group')
        Netlist['Comm_func8'] = Comm
        Comm = Component(type='comment', nodes=[], value='* The coupling coefficients between different L are at the end of the lib file')
        Netlist['Comm_func9'] = Comm
        Netlist['Comm_func_nl'] = Comm_newline

        Comm_space = Component(type='comment', nodes=[], value='*'*150)  # Introduces a frae of stars in the file
        Netlist['Comment_Space_B_Magnet'] = Comm_space
        Comm = Component(type='comment', nodes=[], value='*'*50 + ' MAGNET ' + '*'*80)
        Netlist['Comment_Magnet'] = Comm
        Netlist['Comment_Space_AB_Magnet'] = Comm_space
        # Comments to explain the magnet circuit
        ################################## INITIALIZE MAGNET CIRCUIT ###################################################

        # Calculation of the magnet inductance values for each turn and aperture
        L_magnet = self.__calculate_Inductance_Sections()
        Netlist = self.__generate_magnet_circuit_library(Netlist=Netlist, Nodes=Nodes)

        Netlist['Comment_newline_After_Magnet1'] = Comm_newline
        Netlist['Comment_newline_After_Magnet2'] = Comm_newline

        ################################## COUPLING effects ###################################################

        Netlist['Comment_Space_B_Magnet_2'] = Comm_space
        Comm = Component(type='comment', nodes=[], value='*' * 50 + ' COUPLING OF THE effects ' + '*' * 80)
        Netlist['Comment_eff'] = Comm
        Netlist['Comment_Space_eff'] = Comm_space

        Comm = Component(type='comment', nodes=[], value='* This magnet model is taking into account all the effects that can be seen below')
        Netlist['Comm_func1_eff'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each effect, besides of Wedge and ColdBore, has a different equivalent circuit for each aperture and for each group in that aperture ')
        Netlist['Comm_func2_eff'] = Comm
        Comm = Component(type='comment', nodes=[], value='* The suffix of each element have the format _{aperture}_{group}')
        Netlist['Comm_func6_eff'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each group has a L, R, V and R_gnd')
        Netlist['Comm_func7_eff'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each effect has a number of M FUNC. equal to the number of groups')
        Netlist['Comm_func8_eff'] = Comm
        Comm = Component(type='comment', nodes=[], value='* The values of M FUNC. can be changed thanks to the function change_coupling_parameter in BuilderTFM')
        Netlist['Comm_func9_eff'] = Comm
        Comm = Component(type='comment', nodes=[], value='* Each network model of a group is coupled to all the other network models of the others effects in that group ')
        Netlist['Comm_func12_eff'] = Comm
        Netlist['Comm_func_nl_eff'] = Comm_newline
        Netlist['Comm_func_space_eff'] = Comm_space

        effs = list(self.effects.keys()) # List of all the possible effects that might be included in the magnet
        effs_notCond = self.effs_notCond  # List of the effects that are not conductor losses (Wedge, CB)


        for eff_ind in range(len(effs)): # Looping through all the effects
            eff = effs[eff_ind]
            Comm = Component(type='comment', nodes=[], value='*'*50 + f' EFFECT {eff} ' + '*'*80)
            Netlist[f'Comment_{eff}'] = Comm
            Netlist[f'Comment_{eff}_space_Aft'] = Comm_space

            # Defining the L, M and R functions for each effect and each loop
            Netlist = self.__generate_function_library(Netlist=Netlist, eff=eff, eff_ind=eff_ind)

            for ap in range(1, apertures + 1): # Looping through the apertures
                Comm_Ap = Component(type='comment', nodes=[], value='*'*50 + f' APERTURE {ap} ' + '*'*80 )
                Netlist[f'Comment_{eff}_ap_{ap}'] = Comm_Ap

                # Setting up the Loop library and the couplings with the magnets aperture
                if eff in effs_notCond:
                    Comm_Ap_d = Component(type='comment', nodes=[], value=f'* Coupled {eff} current loop ')
                    Netlist[f'Comment_{eff}_ap_{ap}'] = Comm_Ap_d
                    Netlist = self.__generate_loop_library(Netlist=Netlist, eff=eff, ap=ap, n=ap)
                else:
                    for n in range(1, groups + 1):  # Looping through all the groups in that aperture
                        if sections_to_apertures[n-1] != ap: continue

                        # Initialize the loop comment just if the number of groups != 1 and eff != Wedge and CB
                        Comm_group = Component(type='comment', nodes=[], value='*'*6 + f' LOOP {n} ' + '*'*6)
                        Netlist[f'Comment_{eff}_group_{n}_ap_{ap}_{n}'] = Comm_group
                        Comm_Ap_d = Component(type='comment', nodes=[], value=f'* Coupled {eff} current loop ')
                        Netlist[f'Comment_{eff}_ap_{ap}_{n}'] = Comm_Ap_d

                        Netlist = self.__generate_loop_library(Netlist=Netlist, eff=eff, ap=ap, n=n)

                Netlist[f'Comment_{eff}_{ap}_space_Coup'] = Comm_newline
                # Setting up the couplings with the other effects
                # for the couplings of the components - they couple to all other components and all other sections within this aperture
                for eff_coup_ind in range(eff_ind + 1, len(effs)):
                    eff_coup = effs[eff_coup_ind]
                    Netlist = self.__generate_coupling_library(Netlist=Netlist, eff=eff, eff_coup=eff_coup, ap=ap)

                    Netlist[f'Comment_newline_{eff}_ap_{ap}'] = Comm_newline


            Netlist[f'Comment_newline_{eff}_ap_final'] = Comm_newline
            Netlist[f'Comment_final_space_{eff}'] = Comm_space

        # Computing the mutual coupling between the inductance of the magnet of different groups
        Netlist['comm_mutual'] = Component(type='comment', nodes=[], value='*Mutual coupling between Magnet Inductances')
        Netlist = self.__calculate_MutualInductance_Sections(Netlist=Netlist)

        Netlist['newline_final'] = Comm_newline
        Netlist['space_final'] = Comm_space

        # Initializing the parameters that must be printed on top of the lib file
        Params = {}
        # Initialization of the magnet circuit Inductances
        for key, value in L_magnet.items():
            Params[f'{key}_value'] = value

        Params['T_mag'] = self.temperature
        Params['l_m'] = self.General.magnet_length
        Params['C_ground'] = self.General.C_ground
        Params['L_mag'] = self.General.L_mag
        for eff, value in self.effects.items(): # Flag names and values for each effect
            Params[f'flag_{eff}'] = int(value)

        # circuit_name = self.General.magnet_name + '_TFM'  # Initializing the circuit name as the magnet name + TFM

        # Passing everything to XYCE to write the lib file from the dict of Components
        PX = ParserXYCE(verbose = verbose)
        PX.write_library(output_path=output_path, name=library_name, nodes=Nodes, params=Params, Netlist=Netlist, verbose= verbose)


    def __calculate_Inductance_Sections(self) -> dict:
        '''
        This function initialize the inductance values for each turn for the magnet circuit of the lib file used in XYCE

        :return L: a dictionary with the name and the value of L_mag for each turn
        '''
        M_block = np.array(self.ledet_inputs['M_InductanceBlock_m'])
        fL_L = np.array(self.ledet_inputs['fL_L'])  # Current-dependent effect of the iron on the differential inductance of the magnet
        fL_I = np.array(self.ledet_inputs['fL_I'])  # Current corresponding to fL_L
        length_mag = self.General.magnet_length
        I_magnet = self.General.I_magnet
        turns_to_sections = self.Turns.turns_to_sections
        sections = max(turns_to_sections)
        self.General.inductance_to_section = np.zeros((sections, sections))

        if M_block.all() == 0:
            M_block_path = os.path.join(Path(self.General.local_library_path), f'{self.General.magnet_name}_MutualInductanceMatrix_TFM.csv')
            df = pd.read_csv(M_block_path, skiprows=1, header=None)
            M_block = df.values

        fL = np.interp(I_magnet, fL_I, fL_L)  # Interpolation to calculate the fL_L for our current
        L = {}

        L_sum = 0

        for section in range(1, sections + 1):
            idx = np.where(turns_to_sections == section)[0]  # Finds the indexes of the turns that belong to the current section
            M = M_block[np.ix_(idx, idx)]  # Taking the correct L block corresponding to this aperture
            L_sum_ap_section = np.sum(M) * length_mag * fL
            L_sum += L_sum_ap_section
            ap = int(np.unique(self.Turns.turns_to_apertures[idx])[0])
            L[f'L_{ap}_{section}'] = L_sum_ap_section
            self.General.inductance_to_section[section-1,section-1] = L_sum_ap_section

        self.__setAttribute(self.General, 'L_mag', np.sum(M_block)* length_mag * fL)

        return L


    def __generate_magnet_circuit_library(self, Netlist: dict, Nodes: list) -> dict:
        '''
        This function initialize the magnet circuit for the circuit lib file used in XYCE

        :param Netlist: a dictionary of Components where the new components must be added.
        :param Nodes: a list of 4 nodes corresponding to the ones of the magnet initialization in the circuit yaml file.
        :param L_magnet: a dictionary of Inductances values that must be inserted in the magnet cicruit

        :return Netlist: it returns the updated Netlist with the magnet circuit components

        Nodes: Nodes[0] = Inout, Nodes[1] = mid, Nodes[2] = end, Nodes[3] = GND
        '''

        apertures = self.General.apertures
        sections = max(self.Turns.turns_to_sections)
        sections_to_apertures = self.General.sections_to_apertures
        el_order_to_apertures = self.General.el_order_to_apertures
        el_order_sections = self.General.el_order_sections
        C_g = self.General.C_ground/(self.General.apertures*2)
        R_w = self.General.R_warm /(sections* apertures)
        type = 'standard component'
        Comm_newline = Component(type='comment', nodes=[], value=' ')
        Comm_space = Component(type='comment', nodes=[], value='*'*150)
        section_nodes = {}

        count_nodes = 0 # Starting the node counting
        # Initialize comments for V_ap
        Comm_input_V_ap1 = Component(type='comment', nodes=[], value='* Fake voltage source to easily access the input current')
        Netlist['Comm_input_tap'] = Comm_input_V_ap1

        # Initialize V_ap1 to easily access the input current
        V_ap1 = Component(type=type, nodes=[Nodes[0], f'EE{count_nodes:03d}'], value='0')
        Netlist['V_ap_1'] = V_ap1
        Netlist['Comm_nl_after_input_1'] = Comm_newline

        Netlist[f'C_GND_In'] = Component(type=type, nodes=[f'{Nodes[0]}', f'{Nodes[3]}'], value=f'{C_g}')

        for ap in range(1, apertures + 1): # Looping through the apertures
            # To add the comment 'APERTURE n'
            Comm_Ap = Component(type='comment', nodes=[], value='*'*50 + f' APERTURE {ap} ' + '*'*80)
            Netlist[f'Comment_Magnet_Ap{ap}'] = Comm_Ap
            last_index = len(el_order_to_apertures) - np.flip(el_order_to_apertures).tolist().index(ap) -1
            section_count = 0

            # n_sections = len(np.where(sections_to_apertures==ap)[0])
            # C_g_ap = C_g/(n_sections+1)

            for n in el_order_sections: # Looping for the number of turns
                s_nodes = []
                if sections_to_apertures[n-1] != ap: continue
                if sections != 1: # Adding Turn comment only if number of turns != 1
                    Comm_turning = Component(type='comment', nodes=[], value=f'****** Group {n} ******')
                    Netlist[f'Comment_turning_{ap}_{n}'] = Comm_turning

                # Add C_GND, R_warm, L and V_tap for each subcircuit, considering that
                if ap == 2 and section_count == 0:  # If we are are between one Aperture and the other
                    # the closest V_tap (first of the second Ap) must be attached to the central node
                    V_tap = Component(type=type, nodes=[Nodes[1], f'EE{count_nodes:03d}'], value='0')
                    s_nodes.append(Nodes[1])
                else:
                    # Normal situation
                    V_tap = Component(type=type, nodes=[f'EE{count_nodes:03d}', f'EE{count_nodes + 1:03d}'], value='0')
                    s_nodes.append(f'EE{count_nodes:03d}')
                    count_nodes += 1 # Update node counting
                Netlist[f'V_tap_{ap}_{n}'] = V_tap

                if not self.Options.flag_SC:
                    R_warm = Component(type=type, nodes=[f'EE{count_nodes:03d}', f'EE{count_nodes + 1:03d}'], value=f'{R_w}')
                    count_nodes += 1 # Update node counting
                    Netlist[f'R_warm_{ap}_{n}'] = R_warm

                L_mag = f'L_{ap}_{n}_value'# Take the correct value of L_mag from the input dict

                if ap == 1 and n == el_order_sections[last_index]: # If we are are between one Aperture and the other
                    # 3) the closest L (last of the first Ap) must be attached to the central node
                    L = Component(type=type, nodes=[f'EE{count_nodes:03d}', Nodes[1]], value=f'{L_mag}')
                    s_nodes.append(Nodes[1])
                else:
                    L = Component(type=type, nodes=[f'EE{count_nodes:03d}', f'EE{count_nodes + 1:03d}'], value=f'{L_mag}')
                    s_nodes.append(f'EE{count_nodes + 1:03d}')
                count_nodes += 1 # Update node counting
                Netlist[f'L_{ap}_{n}'] = L
                # Comment in for individual C
                # C_GND = Component(type=type, nodes=[f'EE{count_nodes-1:03d}', f'{Nodes[3]}'], value=f'{C_g_ap}')
                # Netlist[f'C_GND_{ap}_{n}'] = C_GND
                ## Comment in for lumped C
                if ap == 1 and n == el_order_sections[last_index]:
                    C_GND2 = Component(type=type, nodes=[f'{Nodes[1]}', f'{Nodes[3]}'], value=f'{C_g*2}')
                    Netlist[f'C_GND_{ap}_mid'] = C_GND2
                Netlist[f'Comment_newline_Magnet_{ap}_{n}'] = Comm_newline
                section_nodes[n] = s_nodes
                section_count = section_count + 1

                self.print_nodes.append(f'I({self.magnet_circuit_name}:L_{ap}_{n})'.upper())
                self.print_nodes.append(f'V({self.magnet_circuit_name}:EE{count_nodes:03d})'.upper())

        # Comment in for individual C
        # Netlist[f'C_GND_End'] = Component(type=type, nodes=[f'{Nodes[2]}', f'{Nodes[3]}'], value=f'{C_g}')

        # Initialize comments for the last Capacitance and V_ap2
        Netlist[f'Comment_space_Magnet_out'] = Comm_space
        Comm_out_V_ap2 = Component(type='comment', nodes=[],
                                   value='* Fake voltage source to easily access the output current')
        Netlist['Comm_output_tap'] = Comm_out_V_ap2
        # Adding last V_ap2 to complete the circuit
        V_ap2 = Component(type=type, nodes=[f'EE{count_nodes:03d}', Nodes[2]], value='0')
        Netlist['V_ap_2'] = V_ap2
        C_GND = Component(type=type, nodes=[Nodes[2], Nodes[3]], value=f'{C_g}')
        Netlist['C_GND_out'] = C_GND

        ## Introduce the short-circuits across some inductors
        if self.Shorts.sections_to_short:
            if not isinstance(self.Shorts.sections_to_short, list):
                self.Shorts.sections_to_short = [self.Shorts.sections_to_short]
            if not isinstance(self.Shorts.short_resistances, list):
                self.Shorts.short_resistances = [self.Shorts.short_resistances]
            s_count = 0
            for section in self.Shorts.sections_to_short:
                sections_split = section.split('-')
                indices = [np.where(self.General.el_order_sections == element)[0][0] for element in np.array(sections_split).astype(int)]
                sections_split = [element for _, element in sorted(zip(indices, sections_split))]
                if len(sections_split)>1:
                    nodes_short = [section_nodes[int(sections_split[0])][0],section_nodes[int(sections_split[-1])][-1]]
                else:
                    nodes_short = section_nodes[int(section)]
                R_short = self.Shorts.short_resistances[s_count]

                R_com = Component(type=type, nodes=nodes_short, value=f'{R_short}')
                Netlist[f'R_short_Section_{section}'] = R_com
                s_count += 1

        return Netlist


    def __generate_function_library(self, Netlist: dict, eff: str, eff_ind: int) -> dict:
        '''
        This function initialize the function parameter .FUNC for a given effect in the lib file used in XYCE

        :param Netlist: a dictionary of Components where the new components must be added.
        :param eff: name of the effect for which we need the .FUNC parameters
        :param eff_ind: index of this effect fin the effs list

        :return Netlist: it regroups the updated Netlist with the magnet circuit components
        '''

        effs_notCond = self.effs_notCond # effects which are not the conductor losses
        effs = list(self.effects.keys())  # All effects
        groups = self.General.groups
        apertures = self.General.apertures
        sections_to_apertures = self.General.sections_to_apertures

        type_func = 'function'
        default_1 = Component(type=type_func, nodes=['1', ], value='(1.0,1.0) (100000.0,1.0)') # Default function for L, R (default value = 1)
        default_0 = Component(type=type_func, nodes=['1', ], value='(1.0,0.0) (100000.0,0.0)') # Default function for M (default value = 0)
        Comm_newline = Component(type='comment', nodes=[], value=' ')

        # Create the functions for the loops themselves
        for ap in range(1,apertures+1):
            # These are the components that are assumed to be symmetric. Hence, we only need one function for both apertures
            if eff in effs_notCond and eff != 'BS':
                Netlist[f'{eff}_L_1'] = default_1
                Netlist[f'{eff}_R_1'] = default_1
            #  These are the components that are NOT symmetric. Hence we need one function for each aperture
            elif eff == 'BS':
                Netlist[f'{eff}_L_{ap}'] = default_1
                Netlist[f'{eff}_R_{ap}'] = default_1
            else:
                # These are the conductor effects, that need to be created for each section
                for n in range(1,groups+1):
                    # Check if the section also has to be connected to the aperture
                    if sections_to_apertures[n-1] == ap:
                        Netlist[f'{eff}_L_{n}'] = default_1
                        if eff != 'PC': Netlist[f'{eff}_R_{n}'] = default_1
                        Netlist[f'Comment_newline_func_{eff}_{n}'] = Comm_newline
                    else:
                        continue
            for n in range(1, groups + 1):
                Netlist[f'{eff}_M_{n}'] = default_0

        Netlist[f'Comment_newline_func_{eff}_{ap}_{n}_Coupling'] = Comm_newline
        # Create the mutual couplings with all the other effect
        for eff_coup_ind in range(eff_ind + 1, len(effs)): # looping through any effect subsequent to the one given
            eff_coup = effs[eff_coup_ind]
            # These are the components that are assumed to be symmetric. Hence, we only need one function for coupling the component to section n
            if eff in effs_notCond and eff != 'BS':
                for n in range(1, groups + 1):  # looping through the groups
                    if (eff_coup in effs_notCond or eff == 'IFCC'):
                        Netlist[f'M_{eff_coup}_{eff}'] = default_0
                    else: # For all the others we need one M function per loop
                        Netlist[f'M_{eff_coup}_{eff}_{n}'] = default_0
            #  These are the components that are NOT symmetric. Hence we need one function for each aperture
            elif eff == 'BS':
                # The coupling of BS with the other components is assumed to be the same
                if eff_coup in effs_notCond:
                    Netlist[f'M_{eff_coup}_{eff}'] = default_0
                else:
                    for n in range(1, groups + 1):  # looping through the groups
                        Netlist[f'M_{eff_coup}_{eff}_{n}'] = default_0
            # These are the conductor effects, that need to be coupled with each other within their section
            else:
                for n in range(1, groups + 1):  # looping through the groups
                    Netlist[f'M_{eff_coup}_{eff}_{n}'] = default_0
            Netlist[f'Comment_{eff_coup}_{eff}'] = Comm_newline

        return Netlist


    def __generate_loop_library(self, Netlist: dict, eff: str, ap: int, n: int) -> dict:
        '''
        This function initialize the circuit parameter for a given effect in a given aperture and for a given loop of the lib file

        :param Netlist: a dictionary of Components where the new components must be added.
        :param eff: name of the effect for which we need the circuit parameters
        :param ap: index of the aperture
        :param n: index of the groups

        :return Netlist: it returns the updated Netlist with the magnet circuit components
        '''
        effs = self.effects.items()
        type = 'standard component'
        Comm_newline = Component(type='comment', nodes=[], value=' ')
        effs_notCond = self.effs_notCond
        groups = self.General.groups
        sections_to_apertures = self.General.sections_to_apertures

        # If eff == CB or eff == Wedge no need to have multiples circuit component names
        suff = f'{ap}' if eff in effs_notCond else f'{n}'
        if eff == 'BS':
            suff_L = f'{ap}'
        elif eff in effs_notCond:
            suff_L = f'{1}'
        else:
            suff_L = f'{n}'

        if eff != 'PC':  # Assigning L, R, V if eff != 'PC'
            L = Component(type=type, nodes=[f'{eff}_{suff}a', f'{eff}_{suff}b'], value=f'{eff}_L_{suff_L}(1)')
            Netlist[f'L_{eff}_{suff}'] = L
            R = Component(type=type, nodes=[f'{eff}_{suff}b', f'{eff}_{suff}c'], value=f'{eff}_R_{suff_L}(1)')
            Netlist[f'R_{eff}_{suff}'] = R
            V = Component(type=type, nodes=[f'{eff}_{suff}c', f'{eff}_{suff}a'], value='0')
            Netlist[f'V_{eff}_{suff}'] = V
            self.print_nodes.append(f'V({self.magnet_circuit_name}:{eff}_{suff}c)'.upper())
        else:  # If eff == 'PC' add parameter to L and assigns B instead of L
            param = {}
            param['IC'] = f'{eff}_{n}'
            L = Component(type=type, nodes=[f'{eff}_{suff}a', f'{eff}_{suff}b'], value=f'{eff}_L_{suff}(1)', parameters=param)
            Netlist[f'L_{eff}_{suff}'] = L
            I = f'(PC_M_{n}(1)*I(V_tap_{ap}_{n})'
            for eff_c, value in effs:
                if eff == eff_c or not value or eff_c in effs_notCond: continue
                # if eff_c == 'IFCC':
                #     I = I + f'-M_PC_{eff_c}(1)*flag_{eff_c}*I(V_{eff_c}_{n})'
                # else:
                I = I + f'-M_PC_{eff_c}_{n}(1)*flag_{eff_c}*I(V_{eff_c}_{n})'
            I = I + ')'
            B = Component(type='behavioral-current component', nodes=[f'{eff}_{suff}a', f'{eff}_{suff}b'], value=I + f'/{eff}_L_{n}(1)')
            Netlist[f'B_{eff}_{ap}_{n}'] = B
            self.print_nodes.append(f'V({self.magnet_circuit_name}:{eff}_{suff}a)'.upper())
        self.print_nodes.append(f'I({self.magnet_circuit_name}:L_{eff}_{suff})'.upper())
        self.print_nodes.append(f'V({self.magnet_circuit_name}:{eff}_{suff}b)'.upper())

        # Assigning R_gnd for each effect
        R_gnd = Component(type=type, nodes=[f'{eff}_{suff}a', '0'], value='10G')
        Netlist[f'R_gnd_{eff}_{suff}'] = R_gnd

        Netlist[f'Comment_newline_K_{eff}_{suff}'] = Comm_newline
        Comm_Ap_K = Component(type='comment', nodes=[], value=f'* Coupling groups and magnet')
        Netlist[f'Comment_{eff}_{suff}_K'] = Comm_Ap_K

        # Assigning the coupling coefficient between the eff and the inductances of the magnet
        if eff in effs_notCond:
            for i in range(1, groups + 1):
                if sections_to_apertures[i - 1] != ap: continue
                K_value = f'flag_{eff}*{eff}_M_{i}(1)/sqrt(L_{ap}_{i}_value*{eff}_L_{suff_L}(1))'
                K = Component(type=type, nodes=[f'L_{eff}_{ap}', f'L_{ap}_{i}'], value=K_value)
                Netlist[f'K_{eff}_{ap}_{i}'] = K
        else:
            if eff == 'PC' or eff == 'IFCC':  # Assigning K_value depending on superconductive or not (PC and IFCC only exclusively superconductive effects)
                K_value = f'flag_{eff}*{eff}_M_{n}(1)/sqrt(L_{ap}_{n}_value*{eff}_L_{n}(1))*{int(self.Options.flag_SC)}'
            else:
                K_value = f'flag_{eff}*{eff}_M_{n}(1)/sqrt(L_{ap}_{n}_value*{eff}_L_{n}(1))'
            K = Component(type=type, nodes=[f'L_{eff}_{n}', f'L_{ap}_{n}'], value=K_value)
            Netlist[f'K_{eff}_{ap}_{n}'] = K

        return Netlist


    def __generate_coupling_library(self, Netlist: dict, eff: str, eff_coup: str, ap: int) -> dict:
        '''
        This function initialize the mutual coupling coefficients between one eff and another for a given aperture and a given loop

        :param Netlist: a dictionary of Components where the new components must be added.
        :param eff: name of the first effect
        :param eff_coup: name of the coupled effect
        :param ap: index of the aperture
        :param n: index of the loop

        :return Netlist: it returns the updated Netlist with the magnet circuit components
        '''

        effs = list(self.effects.keys()) # All effects
        effs_notCond = self.effs_notCond # effects not conductor losses
        type = 'standard component'
        groups = self.General.groups
        sections_to_apertures = self.General.sections_to_apertures

        # First, let's do the couplings for all component effects
        if eff in effs_notCond:
            # If eff in effs_notCond, but eff_coup in effs_Cond, we have to couple the component to all sections of this aperture
            if eff_coup not in effs_notCond:
                if eff_coup == 'PC':
                    K_coup_value = '0'
                    for i in range(1, groups + 1):
                        K_coup = Component(type=type, nodes=[f'L_{eff}_{ap}', f'L_{eff_coup}_{i}'], value=K_coup_value)
                        Netlist[f'K_{eff_coup}_{eff}_{i}'] = K_coup
                else:
                    for i in range(1,groups+1):
                        if sections_to_apertures[i-1] != ap: continue
                        if eff == 'BS': suff = ap
                        else: suff = 1
                        K_coup_value = f'flag_{eff}*flag_{eff_coup}*M_{eff_coup}_{eff}_{i}(1)/sqrt({eff_coup}_L_{i}(1)*{eff}_L_{suff}(1))'
                        K_coup = Component(type=type, nodes=[f'L_{eff}_{ap}', f'L_{eff_coup}_{i}'], value=K_coup_value)
                        Netlist[f'K_{eff_coup}_{eff}_{i}'] = K_coup
            # If the other effect is also a component, we only have to couple the two aperture-wise loops together
            else:
                suff_eff = ap if eff == 'BS' else '1'
                suff_eff_c = ap if eff_coup == 'BS' else '1'

                K_coup_value = f'flag_{eff}*flag_{eff_coup}*M_{eff_coup}_{eff}(1)/sqrt({eff_coup}_L_{suff_eff_c}(1)*{eff}_L_{suff_eff}(1))'
                K_coup = Component(type=type, nodes=[f'L_{eff}_{ap}', f'L_{eff_coup}_{ap}'], value=K_coup_value)
                Netlist[f'K_{eff_coup}_{eff}_{ap}'] = K_coup
        # Now the couplings between the non-conductor effects -> Only coupled to their own section!
        else:
            for i in range(1, groups + 1):
                if sections_to_apertures[i - 1] != ap: continue
                K_coup_value = f'flag_{eff}*flag_{eff_coup}*M_{eff_coup}_{eff}_{i}(1)/sqrt({eff_coup}_L_{i}(1)*{eff}_L_{i}(1))'
                K_coup = Component(type=type, nodes=[f'L_{eff}_{i}', f'L_{eff_coup}_{i}'], value=K_coup_value)
                Netlist[f'K_{eff_coup}_{eff}_{i}'] = K_coup

        return Netlist


    def __calculate_MutualInductance_Sections(self, Netlist: dict) -> dict:
        '''
        This function initialize the Mutual inductance Coupling coefficient values between each turn for the magnet circuit of the lib file used in XYCE

        :param Netlist: a dictionary of Components where the new components must be added

        :return Netlist: it returns the updated Netlist with the magnet circuit components
        '''
        M_block = np.array(self.ledet_inputs['M_InductanceBlock_m'])
        fL_I = np.array(self.ledet_inputs['fL_I'])
        fL_L = np.array(self.ledet_inputs['fL_L'])
        length_mag = self.General.magnet_length
        I_magnet = self.General.I_magnet
        apertures = self.General.apertures
        type = 'standard component'
        n_Turns = self.General.num_HalfTurns // 2
        turns_to_sections = self.Turns.turns_to_sections
        turns_to_apertures = self.Turns.turns_to_apertures
        sections_to_apertures = self.General.sections_to_apertures
        sections = np.max(turns_to_sections)

        if M_block.all() == 0:
            M_block_path = os.path.join(Path(self.General.local_library_path),f'{self.General.magnet_name}_MutualInductanceMatrix_TFM.csv')
            df = pd.read_csv(M_block_path, skiprows=1, header=None)
            M_block = df.values

        fL = np.interp(I_magnet, fL_I, fL_L)

        if apertures != 1: # Check if either there is more than 1 Ap or more than 1 group, otherwise no coupling
            # Loop to calculate the M for the coupling of different sections in the same aperture
            for ap in range(1, apertures+1):
                # Coupling between different sections of the same aperture
                for group1 in range(1, sections+1):
                    if sections_to_apertures[group1-1] != ap: continue
                    indices1 = np.where(turns_to_sections == group1)[0] # Taking the indices corresponding to group1
                    for group2 in range(group1 + 1, sections + 1):
                        if sections_to_apertures[group2 - 1] != ap: continue
                        indices2 = np.where(turns_to_sections == group2)[0]  # Taking the indices corresponding to group2

                        M_coup = M_block[np.ix_(indices1, indices2)] # Taking the M block corresponding to orix_idx = indices1, vert_idx = indices2
                        K_coup_value = f'{np.sum(M_coup) * (length_mag * fL)}/sqrt(L_{ap}_{group1}_value*L_{ap}_{group2}_value)'
                        K_mag = Component(type=type, nodes=[f'L_{ap}_{group1}', f'L_{ap}_{group2}'], value=K_coup_value)
                        Netlist[f'K_mag_{group1}_{group2}'] = K_mag
                        self.General.inductance_to_section[group1-1, group2-1] = np.sum(M_coup) * (length_mag * fL)
                        self.General.inductance_to_section[group2 - 1, group1 - 1] = np.sum(M_coup) * (length_mag * fL)

        # # Coupling between sections of different apertures
        if apertures == 2: # Only if apertures == 2
            ap = 1
            for group1 in range(1, sections + 1): # All the sections of the 1st ap
                if sections_to_apertures[group1 - 1] != ap: continue
                indices1 = np.where(turns_to_sections == group1)[0] # Taking index of turns that belong to group 1
                for group2 in range(1, sections + 1): # All the sections of the 2nd Ap
                    if sections_to_apertures[group2 - 1] == ap: continue
                    indices2 = np.where(turns_to_sections == group2)[0]  # Taking index of turns that belong to group 2

                    M = M_block[np.ix_(indices1, indices2)]
                    K_coup_value = f'{np.sum(M) * (length_mag * fL)}/sqrt(L_1_{group1}_value*L_2_{group2}_value)'
                    K_mag = Component(type=type, nodes=[f'L_1_{group1}', f'L_2_{group2}'], value=K_coup_value)
                    Netlist[f'K_mag_{group1}_{group2}'] = K_mag
                    self.General.inductance_to_section[group1 - 1, group2 - 1] = np.sum(M) * (length_mag * fL)
                    self.General.inductance_to_section[group2 - 1, group1 - 1] = np.sum(M) * (length_mag * fL)

        return Netlist


    ####################################################################################################################
    ############################################### effects FUNCTIONS ###############################################
    def calculate_PC(self, frequency: np.ndarray, T: float, fMag: np.ndarray, flag_coupling:bool = True, flag_save:bool=False) -> np.ndarray:
        '''
        Function that calculates the equivalent circuit parameter for the persistent currents and save them to the
        PC dataclass

        :param frequency: Frequency vector
        :param T: temperature vector, to be used in the interaction with Eddy-currents
        :param fMag: field-factor for each strand
        :param flag_coupling: if True it means it has to be coupled to another effect
        :param flag_save: if True saves the circuit parameter in the PC dataclass
        '''

        l_magnet = self.General.magnet_length
        ds_filamentary = self.Strands.d_filamentary
        dws = self.Strands.diameter
        RRR = self.Strands.RRR
        n_strands = np.sum(self.HalfTurns.n_strands)
        strands_to_conductor = self.Strands.strands_to_conductor

        # Calculating constants
        w = 2 * np.pi * frequency.reshape(len(frequency), 1)

        B = self.General.I_magnet*fMag
        rho_el_0 = self.__rhoCu_nist(T=T, RRR=RRR, B=B[0, :])

        tb_strand = dws - ds_filamentary

        # Calculate the equivalent circuit parameter
        tau_ed = self.mu0 / 2 * (dws / 2 * tb_strand / 2) / rho_el_0

        if flag_coupling:
            alpha2 = 1 / np.sqrt(np.sqrt((1 + (w * tau_ed) ** 2)))
        else:
            alpha2 = np.ones(w.shape)

        M_temp = (np.pi / 4 * l_magnet * ds_filamentary * fMag * alpha2)
        Lm = np.array([self.mu0 * np.pi / 4 * l_magnet] * len(frequency))
        M_if_Pc = self.mu0 * np.pi / 8 * l_magnet


        # M_pc = np.sqrt(np.sum(M_temp[:, idx_valid], axis=1))
        L_repeated = np.tile(Lm, n_strands)
        L_pc = np.reshape(L_repeated, (len(frequency), n_strands), order='F')
        STC_pc = np.repeat(strands_to_conductor[:,np.newaxis], len(frequency), axis=1).T
        I_Pc = np.array([0]*len(frequency))
        I_Pc = np.tile(I_Pc, n_strands)
        I_Pc = np.reshape(I_Pc, (len(frequency), n_strands), order='F')

        L_pc = np.squeeze(L_pc)
        STC_pc = np.squeeze(STC_pc)
        M_temp = np.squeeze(M_temp)

        L_group, R_group, M_group, I_group = self.__group_components(frequency=frequency, L=L_pc, R=STC_pc, M=M_temp, sort_on='strands', I=I_Pc)

        M_group = self.__adjust_M_for_short(M_group)
        if flag_save:
            self.__setAttribute(self.PC, 'M', M_group)
            self.__setAttribute(self.PC, 'I', I_group)
            self.__setAttribute(self.PC, 'L', L_group)
            self.__setAttribute(self.PC, 'M_PC_IFCC', M_if_Pc)
            self.__setAttribute(self.PC, 'M_strands', M_temp)
        else:
            return  M_temp, I_Pc


    def calculate_IFCC(self, frequency: np.ndarray, T: float, fMag: np.ndarray, flag_coupling: bool = True, flag_save: bool = False) -> np.ndarray:
        '''
        Calculates the equivalent IFCL coupling loops for a given temperature and field

        :param frequency: Frequency vector
        :param T: temperature vector
        :param fMag: field-factor for each strand
        :param flag_coupling: if True it means it has to be coupled to another effect
        :param flag_save: if True saves the circuit parameter in the IFCC dataclass
        '''

        w = 2 * np.pi * frequency.reshape(len(frequency), 1)

        # Setting all required parameters for the MB magnet
        f_ro_eff = self.Strands.f_rho_effective
        l_mag = self.General.magnet_length
        dws = self.Strands.diameter
        ds_filamentary = self.Strands.d_filamentary
        RRR = self.Strands.RRR
        Lp_f = self.Strands.fil_twist_pitch
        groups = self.General.groups


        mu0_eff = self.mu0  #* (1 - fsc)

        # Resistivity calculations
        B = self.General.I_magnet*fMag
        rho_el_0 = self.__rhoCu_nist(T=T, RRR=RRR*f_ro_eff, B=B[0, :]) + 1e-12
        rho_el_Outer = self.__rhoCu_nist(T=T, RRR=RRR, B=B[0, :]) + 1e-12

        # Calculating the coupled loop equivalent parameter
        beta_if = (Lp_f / (2 * np.pi)) ** 2 * 1 / (rho_el_0)
        tau_if = mu0_eff / 2 * beta_if

        tb_strand = dws - ds_filamentary
        # tau_ed = self.mu0 / 8 * (dws / 2) ** 2  / rho_el_Outer
        tau_ed = self.mu0 / 2 * (ds_filamentary / 2 * tb_strand / 2) / rho_el_Outer
        if flag_coupling:
            tau = tau_if+tau_ed
            beta_if = 2 * tau / mu0_eff
        else:
            tau = tau_if
        alpha = 1 / np.sqrt((1 + (w * (tau)) ** 2))
        dB = w * fMag * alpha

        # Standard method
        I_if = beta_if * ds_filamentary * dB
        P_if = 1/2*beta_if * (ds_filamentary/2) **2 * np.pi * l_mag *  dB**2
        # Power formula proposed in Arjans thesis - not working in XYCE
        # I_if = np.sqrt(np.pi / (2*w)) * beta_if * dS * dB
        # P_if = 2*dS**2*l_mag*np.pi/4*(2*tau_if*np.pi*w)/self.mu0*(f_mag*alpha)**2

        I_tot_im = I_if * alpha
        I_tot_re = I_if * alpha * w * tau
        # I_tot_re = np.sqrt(I_if ** 2 - I_tot_im ** 2)
        I_if = I_tot_re + 1j * I_tot_im

        R_if = P_if / np.real((I_if * np.conjugate(I_if)))
        L_if = np.ones((len(frequency), 1)) * tau * R_if[0, :]
        M_if = (1j * w.reshape(len(frequency), 1) * L_if * I_if + I_if * R_if) / (1j * w.reshape(len(frequency), 1) * 1)

        R_if = np.squeeze(R_if)
        L_if = np.squeeze(L_if)
        M_if = np.squeeze(M_if)
        I_if = np.squeeze(I_if)

        L, R, M, I = self.__group_components(frequency, L_if, R_if, M_if, sort_on='strands', I=I_if)

        M = self.__adjust_M_for_short(M)
        if flag_save:
            self.__setAttribute(self.IFCC, 'M',  M)
            self.__setAttribute(self.IFCC, 'R', R)
            self.__setAttribute(self.IFCC, 'L', L)
            self.__setAttribute(self.IFCC, 'I', I)
            self.__setAttribute(self.IFCC, 'P', P_if)
            self.__setAttribute(self.IFCC, 'tau', tau_if)
            self.__setAttribute(self.IFCC, 'M_strands',  M_if)
            self.__setAttribute(self.IFCC, 'R_strands', R_if)
            self.__setAttribute(self.IFCC, 'I_strands', I_if )
        else:
            return M_if, I_if


    def calculate_ISCC(self, frequency: np.ndarray, T: float, fMag_X: np.ndarray, fMag_Y: np.ndarray, flag_save: bool = False) -> np.ndarray:
        '''
        Function that calculates the power loss and induced currents by ISCL and derives the equivalent circuit parameter

        :param frequency: Frequency vector
        :param T: temperature vector
        :param fMag_X: field-factor along X axis for each strand
        :param fMag_Y: field-factor along Y axis for each strand
        :param flag_save: if True saves the circuit parameter in the ISCC dataclass

        :return f_mag_X_return: return field-factor along X axis for each strand
        :return fMag_Y: return field-factor along Y axis for each strand
        '''
        f = frequency
        w = 2 * np.pi * f.reshape(len(f), 1)  #

        l_mag = self.General.magnet_length

        dws = self.HalfTurns.diameter
        rotation_block = self.HalfTurns.rotation_ht
        mirror_block = self.HalfTurns.mirror_ht
        alphasRAD = self.HalfTurns.alphaDEG_ht * np.pi / 180
        fsc = self.HalfTurns.fsc
        n_strands = self.HalfTurns.n_strands
        n_HT = self.General.num_HalfTurns
        Lp_s = self.HalfTurns.strand_twist_pitch
        wBare = self.HalfTurns.bare_cable_width
        hBare = self.HalfTurns.bare_cable_height_mean
        Nc = self.HalfTurns.Nc
        C = self.HalfTurns.C_strand
        R_c = self.HalfTurns.Rc
        RRR = self.HalfTurns.RRR
        f_ro_eff = self.HalfTurns.f_rho_effective

        inverse_field = int(n_HT / 4) * [1] + int(n_HT / 4) * [-1] + int(n_HT / 4) * [1] + int(n_HT / 4) * [-1]
        inverse_field = np.repeat(inverse_field, n_strands)
        alphas_ht = np.zeros(np.sum(n_strands),)
        tempS = 0

        for h in range(len(alphasRAD)):
            if mirror_block[h] == 0:
                alphas_ht[tempS:tempS + n_strands[h]] = alphasRAD[h] - rotation_block[h] / 180 * np.pi
            elif mirror_block[h] == 1:
                alphas_ht[tempS:tempS + n_strands[h]] = np.pi / 2 - alphasRAD[h] - rotation_block[h] / 180 * np.pi
            tempS = tempS + n_strands[h]

        f_magPerp = (-fMag_X * np.sin(alphas_ht) + fMag_Y * np.cos(alphas_ht))
        f_magPerp = np.transpose(inverse_field * f_magPerp)

        r_magPerp = np.transpose(fMag_X * np.cos(alphas_ht) + fMag_Y * np.sin(alphas_ht))
        B_temp = np.sqrt(fMag_X ** 2 + fMag_Y ** 2).T

        ## Reverse action:
        ## fMag_X = r_magPerp.T*np.cos(alphas)-f_magPerp.T*np.sin(alphas)
        ## fMag_Y = r_magPerp.T*np.sin(alphas)+f_magPerp.T*np.cos(alphas)

        f_magPerp_ht = np.zeros((n_HT, len(frequency)))
        r_magPerp_ht = np.zeros((n_HT, len(frequency)))
        B_ht = np.zeros((n_HT, len(frequency)))
        tempS = 0
        for i in range(len(n_strands)):
            f_magPerp_ht[i] = np.average(f_magPerp[tempS:tempS + n_strands[i], :], axis=0)
            r_magPerp_ht[i] = np.average(r_magPerp[tempS:tempS + n_strands[i], :], axis=0)
            B_ht[i] = np.average(B_temp[tempS:tempS + n_strands[i], :], axis=0)
            tempS = tempS + n_strands[i]

        alpha_c = wBare / hBare
        # rho_C_Strands = R_c / (rho_el_Outer * (n_strands ** 2 - n_strands) / (2 * Lp_s * alpha_c)) #Eq. 4.33 in Arjans Thesis p. 78

        #  Calculating the equivalent circuit parameter
        beta_is = 1 / 120 * Lp_s / R_c * n_strands * (n_strands - 1) * wBare / hBare
        
        # tau_is = self.mu0 * beta_is
        factor_tau = alpha_c * Nc / (alpha_c + C * (Nc - 1))  # Eq. 4.41 in Arjans Thesis p.89
        tau_is = self.mu0*beta_is
        # tau_is = 1.65e-08 * (Lp_s * (n_strands ** 2 - 4 * n_strands)) / R_c * factor_tau  # Eq. 4.31 in Arjans Thesis p.78

        alpha = 1 / np.sqrt((1 + (w * tau_is) ** 2))
        dB = w * f_magPerp_ht.T * alpha

        P_is = 1/2*l_mag * beta_is * dB ** 2 * wBare * hBare
        I_is = beta_is * hBare * dB

        I_tot_im = I_is * alpha
        I_tot_re = I_is * alpha * w * tau_is
        #I_tot_re = np.sqrt(I_is ** 2 - I_tot_im ** 2)
        I_is = I_tot_re + 1j * I_tot_im

        # Calculate equivalent parameter
        R_is = P_is / np.real((I_is*np.conjugate(I_is)))
        L_is = np.ones((len(f),1))* tau_is * R_is[0,:]
        M_is = (1j * w.reshape(len(f), 1) * L_is * I_is + I_is * R_is) / (1j * w.reshape(len(f), 1) * 1)
        # M_is = np.sqrt(np.real(M_is) ** 2 + np.imag(M_is) ** 2)

        # Calculate warm resistance of a strand-pitch
        if not self.Options.flag_SC:
            ## Add the warm part to account for ISCL in non-superconducting state
            rho_el_Outer = self.__rhoCu_nist(T, B_ht[:, 0], RRR*f_ro_eff) + 1e-12
            alpha_st = np.arctan(wBare/(Lp_s/2)) #Half twist-pitch as Lp is the full length until its back at the beginning
            l_strand = 2 * wBare / np.sin(alpha_st) + 2 * hBare  # twice as we go back AND forth
            A_strand = (1 - fsc) * np.pi * (dws / 2) ** 2
            R_strand = rho_el_Outer * l_strand / A_strand
            alpha_c = wBare / hBare
            rho_C_Strands = R_c / (rho_el_Outer * (n_strands ** 2 - n_strands) / (
                        2 * Lp_s * alpha_c))  # Eq. 4.33 in Arjans Thesis p. 78
            alpha_c = wBare / hBare

            R_c_warm = 2e-3 * rho_C_Strands * rho_el_Outer * (n_strands** 2 - n_strands) / (2 * Lp_s * alpha_c)
            R_c_N = R_c_warm + R_strand
            # fT = 1/(1.9)**0.08*T**(0.08)
            # fT = 2*1/(np.log(1.9)**0.186)*np.log(T)**0.186
            fT = 1 / (np.log(1.9) ** 0.186) * np.log(T) ** 0.186
            # fT = 1 / (np.log(1.9) ** 0.3179) * np.log(T) ** 0.3179
            R_c_warm = R_c * fT
            R_c_N = fT * (R_c_warm + R_strand)

            tau_is_N = np.zeros(Nc.shape)
            factor_tau = alpha_c * Nc / (alpha_c + C * (Nc - 1))  # Eq. 4.41 in Arjans Thesis p.89
            for i in range(len(tau_is_N)):
                if Nc[i] >= 8:
                    tau_is_N[i] = 1.65e-8 * C[i] * (Lp_s[i] * (n_strands[i] ** 2 - 4 * n_strands[i])) / R_c_N[i] * factor_tau[
                        i]  # Eq. 4.31 in Arjans Thesis p.78
                else:
                    tau_is_N[i] = self.mu0 * beta_is[i]
            # tau_is_N = 1.65e-8*C*2/(fT) * (Lp_s*(nS**2-4*nS))/R_c_N *factor_tau # Equation 4.31 in Arjans Thesis P.78 and Eq. 4.41
            # beta_is_N = tau_is_N/ self.mu0
            beta_is_N = 1 / 120 * Lp_s / R_c_N * n_strands * (n_strands - 1) * wBare / hBare  # 60 works well for 290 K

            ## Adjust the components again on the new time constant
            alpha = 1 / np.sqrt((1 + (w * tau_is_N) ** 2))
            dB = w * f_magPerp_ht.T * alpha

            P_is = l_mag * beta_is_N * dB ** 2 * wBare * hBare
            I_is = beta_is_N * hBare * dB
            # I_is = 1 / 12 * Lp_s / R_c * wBare * dB * (nS ** 2 - 1) / nS
            I_tot_im = I_is * alpha
            # I_tot_re = np.sqrt(I_is ** 2 - I_tot_im ** 2)
            I_tot_re = I_is * alpha * w * tau_is_N
            I_is = I_tot_re + 1j * I_tot_im

            # Calculate equivalent parameter
            R_is = P_is / np.real((I_is * np.conjugate(I_is)))
            L_is = np.ones((len(f), 1)) * tau_is_N * R_is[0, :]
            M_is = (1j * w.reshape(len(f), 1) * L_is * I_is + I_is * R_is) / (1j * w.reshape(len(f), 1) * 1)
            # M_is = np.sqrt(np.real(M_is) ** 2 + np.imag(M_is) ** 2)

        # ## Calculate the return field
        # Assuming a current line on each side of the cable
        # Average distance to each strand is hence: (1/2*(dws/2 + (nS/2-1)*dws)), neglecting hBare
        # Twice, as we have one line on each side -> both generating the same field
        # B_return = (2 * (self.mu0 * np.abs(I_is)) / np.pi * 1 / (1 / 2 * (dws / 2 + (n_strands / 2 - 1) * dws)))
        # dB_return = (B_return/tau_is)

        # f_mag_X_return_ht = r_magPerp_ht*np.cos(alphas_ht)-B_return.T*np.sin(alphas_ht)
        # f_mag_Y_return_ht = r_magPerp_ht*np.sin(alphas_ht)+B_return.T*np.cos(alphas_ht)
        # ratio_Breturn = B_return / B_ht.T

        f_mag_X_return = np.zeros((len(f), fMag_X.shape[1]))
        f_mag_Y_return = np.zeros((len(f), fMag_Y.shape[1]))

        temp_c = 0
        for i in range(len(n_strands)):
            for j in range(int(n_strands[i] / 2)):
                ratio_Breturn1 = ((self.mu0 * np.abs(I_is[:, i])) / (4*np.pi) * 1 / ((dws[i] / 2 + j * dws[i])))
                ratio_Breturn2 = ((self.mu0 * np.abs(I_is[:, i])) / (4*np.pi) * 1 / ((dws[i] / 2 + (int(n_strands[i] / 2) - j) * dws[i])))
                ratio_Breturn = ratio_Breturn1 + ratio_Breturn2
                f_mag_X_return[:, temp_c] = ratio_Breturn / B_temp[temp_c, :] * fMag_X[:, temp_c]
                f_mag_Y_return[:, temp_c] = ratio_Breturn / B_temp[temp_c, :] * fMag_Y[:, temp_c]
                f_mag_X_return[:, temp_c + 1] = ratio_Breturn / B_temp[temp_c + 1, :] * fMag_X[:, temp_c + 1]
                f_mag_Y_return[:, temp_c + 1] = ratio_Breturn / B_temp[temp_c + 1, :] * fMag_Y[:, temp_c + 1]
                temp_c = temp_c + 2

        R_is = np.squeeze(R_is)
        L_is = np.squeeze(L_is)
        M_is = np.squeeze(M_is)
        I_is = np.squeeze(I_is)
        P_is = np.squeeze(P_is)

        L, R, M, I = self.__group_components(f, L_is, R_is, M_is, sort_on='HalfTurns', I=I_is)
        M = self.__adjust_M_for_short(M)

        if flag_save:
            self.__setAttribute(self.ISCC, 'M', M)
            self.__setAttribute(self.ISCC, 'R', R)
            self.__setAttribute(self.ISCC, 'L', L)
            self.__setAttribute(self.ISCC, 'P', P_is)
            self.__setAttribute(self.ISCC, 'I', I)
            self.__setAttribute(self.ISCC, 'M_halfturns', M_is)
            self.__setAttribute(self.ISCC, 'R_halfturns', R_is)
            self.__setAttribute(self.ISCC, 'I_halfturns', I_is )
            if not self.Options.flag_SC:
                self.__setAttribute(self.ISCC, 'tau', tau_is_N)
            else:
                self.__setAttribute(self.ISCC, 'tau', tau_is)
        else:
            return M_is, I_is, f_mag_X_return, f_mag_Y_return


    def calculate_ED(self, frequency: np.ndarray, T: float, fMag: np.ndarray, flag_coupling: bool = True, flag_save: bool = False) -> np.ndarray:
        '''
        Calculates the equivalent coupling loops in the outer copper sheet for a given temperature and field

        :param frequency: Frequency vector
        :param T: temperature vector
        :param fMag: field-factor for each strand
        :param flag_coupling: if True it means it has to be coupled to another effect
        :param flag_save: if True saves the circuit parameter in the ED dataclass
        '''

        f = frequency
        w = 2 * np.pi * f.reshape(len(f), 1)

        l_mag = self.General.magnet_length
        RRR = self.Strands.RRR
        rws = self.Strands.diameter / 2

        if not self.Options.flag_SC:  # TODO - check if needed or not
            r_filamentary = self.Strands.d_filamentary / 2 * 0.5
        else:
            r_filamentary = self.Strands.d_filamentary / 2


        B = self.General.I_magnet * fMag
        rho_el_0 = self.__rhoCu_nist(T=T, B=B[0, :], RRR=RRR) + 1e-12
        tb_strand = rws - r_filamentary
        rho_el_0 = rho_el_0 + 1e-12

        # Calculating time constant, correction factor and field derivative
        tau_ed = self.mu0 / 2 * ((rws) * tb_strand) / rho_el_0
        # tau_ed = self.mu0 / 8 * dws**2 / rho_el_0 ## Formula from Turck79
        alpha = 1 / np.sqrt((1 + (w * tau_ed) ** 2))
        dB = w * fMag

        # Skindepth
        skinDepth = np.sqrt(2 * rho_el_0 / (w * self.mu0))
        idx_s = np.argmin(abs(skinDepth - (1 - 1 / np.exp(1)) * tb_strand), axis=0) + 1

        # Calculating the power loss
        P_DC = l_mag * np.pi/(8*rho_el_0) * rws **4 *(dB * alpha) ** 2
        # P_DC = tau_ed/self.mu0/2 * (1-(dS_inner/dws)**2) * (dB*alpha)**2 # Formula from Turck
        # P_DC = v3 * v1v2/(v1v2+1)*beta_if*(dB*alpha)**2 # Formula from Arjan's thesis

        P_AC = l_mag * np.pi / (2*rho_el_0) * rws * skinDepth ** 3 * (dB) ** 2
        # P_AC = dB ** 2 * skinDepth/(w*4*self.mu0*dws) #Formula from Turck1979

        # Calculating the induced current
        I_DC = rws ** 3 / (3 * rho_el_0) * (dB * alpha)
        # I_DC = 2 * tb_strand / (3 * rho_el_0) * (tb_strand ** 2 - 3 * tb_strand * dS_outer + 3 * dS_outer ** 2) * (dB * alpha)
        # I_DC = 2 * tau_ed / self.mu0 * dS_outer * (dB*alpha)
        I_DC_im = I_DC * alpha
        I_DC_re = I_DC * alpha * w * tau_ed
        # I_tot_re = np.sqrt(I_tot ** 2 - I_tot_im ** 2)
        I_DC = I_DC_re + 1j * I_DC_im

        I_tot = I_DC
        # I_tot = np.zeros((I_DC.shape), dtype=np.complex_)
        # for j in range(I_tot.shape[1]):
        #     fac = np.sqrt(w[idx_s[j]:]) / np.sqrt(w[idx_s[j]])
        #     I_t = [I_DC[:idx_s[j], j], I_DC[idx_s[j]:, j] * fac[:, 0]]
        #     I_tot[:, j] = np.concatenate(I_t).ravel()

        P_tot = np.zeros((P_DC.shape))
        for j in range(P_DC.shape[1]):
            P_t = [P_DC[:idx_s[j], j], P_AC[idx_s[j]:, j]]
            P_tot[:, j] = np.concatenate(P_t).ravel()
        P_tot = 1/2*P_tot

        P_tot = np.squeeze(P_tot)
        I_ed = np.squeeze(I_tot)
        tau_ed = tau_ed

        # Calculating the coupled loop equivalent parameter
        R_ed = P_tot / np.real(I_ed * np.conjugate(I_ed))
        L_ed = np.ones((len(f), 1)) * tau_ed * R_ed[0, :]
        M_ed = (1j * w * L_ed * I_ed + I_ed * R_ed) / (1j * w * 1)
        # M_ed = np.real(M_ed) ** 2 + np.imag(M_ed) ** 2

        L, R, M, Ied = self.__group_components(f, L_ed, R_ed, M_ed, sort_on='strands', I=I_ed)
        M = self.__adjust_M_for_short(M)

        if flag_save:
            self.__setAttribute(self.ED, 'M', M)
            self.__setAttribute(self.ED, 'R', R)
            self.__setAttribute(self.ED, 'L', L)
            self.__setAttribute(self.ED, 'P', P_tot)
            self.__setAttribute(self.ED, 'I', Ied)
            self.__setAttribute(self.ED, 'tau', tau_ed)
            self.__setAttribute(self.ED, 'M_strands', M_ed)
            self.__setAttribute(self.ED, 'R_strands', R_ed)
            self.__setAttribute(self.ED, 'I_strands', I_ed)
        else:
            return M_ed, I_ed


    def calculate_CB(self, T: float):
        '''
        Function that calculates the equivalent parameter for eddy currents in the cold bore.
        It takes the Temperature. It then calculates the resistivity and
        __interpolates the current and power from Comsol model that includes the ColdBore effect.

        :param T: Temperature vector
        '''
        if not isinstance(self.CB.f_SS, (int,float)):
            self.CB.f_SS = 1
        if not isinstance(self.CB.r_CB, (int,float)) or not isinstance(self.CB.t_CB, (int,float)):
            raise Exception('flag_CB is on. Please provide thickness t_CB and radius r_CB')

        f = self.frequency
        w = 2 * np.pi * f
        rho_CB = self.__rhoSS_nist(T=T)*self.CB.f_SS

        r_CB = self.CB.r_CB #0.052
        t_CB = self.CB.t_CB #0.0015
        l_mag = self.General.magnet_length
        fm = self.B_nom_center / self.ledet_options.Iref

        tau_CB = self.mu0 / 2 * (r_CB) * t_CB / rho_CB
        # tau_CB = 3.3e-5

        skinDepth = np.sqrt(2 * rho_CB / (w * self.mu0))
        idx_s = np.argmin(abs(skinDepth - (1 - 1 / np.exp(1)) * t_CB), axis=0) + 1
        if idx_s >= len(f): idx_s = len(f) - 1

        dB = w * fm
        alpha = 1 / np.sqrt((1 + (w * tau_CB) ** 2))

        # Calculating the power loss
        P_DC = ((r_CB) ** 4 - (r_CB - t_CB) ** 4) / (4 * rho_CB) * (dB * alpha) ** 2 * np.pi
        P_AC = skinDepth ** 3 / (2 * rho_CB) * dB ** 2 * np.pi * (r_CB)
        P_tot = [P_DC[:idx_s], P_AC[idx_s:]]
        P_tot = np.concatenate(P_tot).ravel() * l_mag

        I_tot = 2 * t_CB / (3 * rho_CB) * (t_CB ** 2 - 3 * t_CB * r_CB + 3 * r_CB ** 2) * (dB * alpha)
        I_tot_im = I_tot * alpha
        I_tot_re = (I_tot * alpha * w * tau_CB)
        # I_tot_re = np.sqrt(I_tot ** 2 - I_tot_im ** 2)
        I_tot = I_tot_re + 1j * I_tot_im

        fac = np.sqrt(w[idx_s:]) / np.sqrt(w[idx_s])
        I_tot = [I_tot[:idx_s], I_tot[idx_s:] * fac]
        I_tot = np.concatenate(I_tot).ravel()

        # Calculating the coupled loop equivalent parameter
        R_cb = P_tot / np.real((I_tot * np.conjugate(I_tot)))
        L_cb = tau_CB * R_cb[0]
        M_cb = (1j * w * L_cb * I_tot + I_tot * R_cb) / (1j * w * 1)
        # M_cb = np.sqrt(np.real(M_cb*np.conjugate(M_cb))) # Checked: is the same as the line below
        # M_cb = np.sqrt(np.real(M_cb) ** 2 + np.imag(M_cb) ** 2)
        M_cb = np.transpose(np.ones(M_cb.shape).transpose() * M_cb[0])
        L_cb = np.repeat(L_cb, len(R_cb))

        self.__setAttribute(self.CB, 'P', P_tot)
        self.__setAttribute(self.CB, 'I', I_tot)
        self.__setAttribute(self.CB, 'tau', tau_CB)
        self.__setAttribute(self.CB, 'L', L_cb)
        self.__setAttribute(self.CB, 'R', R_cb)
        self.__setAttribute(self.CB, 'M', M_cb)


    def calculate_BS(self):
        '''
        Function that calculates the equivalent parameter for eddy currents in the beam screen.
        '''
        if not isinstance(self.BS.r_BS, (int,float)):
            raise Exception('flag_BS on but no BS parameter provided.')
        if not isinstance(self.BS.f_SS, (int,float)):
            self.BS.f_SS = 1

        frequency = self.frequency
        w = 2 * np.pi * frequency

        # Setting up the required parameter for the MB-magnet
        I = self.TFM_inputs.current
        if isinstance(self.BS.T_BS, (int, float)):
            T = self.BS.T_BS
        else:
            T = 20
        factor_SS = self.BS.f_SS
        fm = self.B_nom_center / self.ledet_options.Iref
        l_mag = self.General.magnet_length

        apertures = ['A', 'B']
        R_BS = []
        L_BS = []
        M_BS = []
        I_BS = []
        P_BS = []
        tau_BS = []
        for aperture in apertures:
            rho_Cu_Inner = self.__rhoCu_nist(np.array([T]), np.array([self.__getAttribute('BS', f'RRR_Ap{aperture}_1')]), np.array([fm * I]))
            rho_Cu_Outer = self.__rhoCu_nist(np.array([T]), np.array([self.__getAttribute('BS', f'RRR_Ap{aperture}_2')]), np.array([fm * I]))
            rho_SS = self.__rhoSS_nist(T)*factor_SS
            tb_1 = self.__getAttribute('BS', f't_Ap{aperture}_1')
            tb_2 = self.__getAttribute('BS', f't_Ap{aperture}_2')
            tb_S = self.__getAttribute('BS', f't_SS_{aperture}')
            
            R = self.BS.r_BS # - tb_1 - tb_2 - tb_S
            R_eq = self.BS.r_BS * 1.0798  ##Not the actual radius but an equivalent one, Correction factor of 1.08 valid for LHC main dipole !!!

            ## Derivation of the induced current
            # Layer 1
            skinDepth_1 = np.sqrt(2 * rho_Cu_Inner / (w * self.mu0))
            idx_s1 = min(np.argmin(abs(skinDepth_1 - (1 - 1 / np.exp(1)) * tb_1)) + 1, len(frequency) - 1)

            tau_DC1_dyn = self.mu0 / 2 * R_eq * skinDepth_1 * (1 - np.exp(-tb_1 / skinDepth_1)) / rho_Cu_Inner
            tau_DC1_dyn = [tau_DC1_dyn[:idx_s1], [tau_DC1_dyn[idx_s1]] * (len(frequency) - idx_s1)]
            tau_DC1_dyn = np.concatenate(tau_DC1_dyn).ravel()
            alpha_DC1_dyn = 1 / np.sqrt(1 + (w * tau_DC1_dyn) ** 2)

            tau_DC1_sta = self.mu0 / 2 * R_eq * (tb_1) / rho_Cu_Inner
            alpha_DC1_sta = 1 / np.sqrt(1 + (w * tau_DC1_sta) ** 2)
            P_DC_1 = np.pi * (fm * w * alpha_DC1_sta) ** 2 * 1 / 4 * (1 / rho_Cu_Inner * ((R) ** 4 - (R - tb_1) ** 4))
            P_AC_1 = skinDepth_1 ** 2 / (2 * rho_Cu_Inner) * (fm * w) ** 2 * np.pi * (skinDepth_1) * (R - tb_2 - tb_S)
            P_1 = [P_DC_1[:idx_s1], P_AC_1[idx_s1:]]
            P_1 = np.concatenate(P_1).ravel()

            # Layer 2
            skinDepth_2 = np.sqrt(2 * rho_Cu_Outer / (w * self.mu0))
            # idx_s2 = np.argmin(abs((tb_2)-skinDepth_2))+1
            idx_s2 = min(np.argmin(abs(skinDepth_2 - (1 - 1 / np.exp(1)) * tb_2)), len(frequency) - 1)

            P_DC_2a = np.pi * (fm * w * alpha_DC1_dyn) ** 2 * 1 / 4 * (1 / rho_Cu_Outer * ((R - tb_S) ** 4 - (R - tb_2 - tb_S) ** 4))
            P_DC_2b = np.pi * (fm * w * alpha_DC1_dyn[idx_s1]) ** 2 * 1 / 4 * (1 / rho_Cu_Outer * ((R - tb_S) ** 4 - (R - tb_2 - tb_S) ** 4))
            P_AC_2 = skinDepth_2 ** 2 / (2 * rho_Cu_Outer) * (fm * w )** 2 * np.pi * (skinDepth_2) * (R - tb_S)

            P_2 = [P_DC_2a[:idx_s1], P_DC_2b[idx_s1:idx_s2], P_AC_2[idx_s2:]]
            P_2 = np.concatenate(P_2).ravel()

            # Layer 3
            skinDepth_3 = np.sqrt(2 * rho_SS / (w * self.mu0))
            idx_s3a = min(np.argmin(abs(alpha_DC1_dyn - 0.05)) - 1, len(frequency) - 1)
            idx_s3b = min(np.argmin(abs(tb_S - skinDepth_3)) - 1, len(frequency) - 1)
            if idx_s3a > idx_s3b: idx_s3b = idx_s3a

            P_DC_3a = np.pi * (fm * w * alpha_DC1_dyn) ** 2 * 1 / 4 * (1 / rho_SS * ((R) ** 4 - (R - tb_S) ** 4))
            P_DC_3b = np.pi * (fm * w * alpha_DC1_dyn[idx_s3a]) ** 2 * 1 / 4 * (1 / rho_SS * ((R) ** 4 - (R - tb_S) ** 4))
            P_AC_3 = skinDepth_3 ** 3 / (2 * rho_SS) * (fm * w) ** 2 * np.pi * R

            P_3 = [P_DC_3a[:idx_s3a], P_DC_3b[idx_s3a:idx_s3b], P_AC_3[idx_s3b:]]
            P_3 = np.concatenate(P_3).ravel()

            ###
            P_tot = P_1 + P_2 + P_3
            P_tot = l_mag * P_tot

            ## Derivation of the induced current
            I_DC1 = 2 * (tb_1) / (3 * rho_Cu_Inner) * ((tb_1) ** 2 - 3 * (tb_1) * R + 3 * R ** 2) * (fm * w * alpha_DC1_sta)
            I_DC1_im = I_DC1 * alpha_DC1_sta
            R2 = R - tb_S
            I_DC2 = 2 * (tb_2) / (3 * rho_Cu_Outer) * ((tb_2) ** 2 - 3 * (tb_2) * R2 + 3 * R2 ** 2) * (fm * w * alpha_DC1_sta)
            I_DC2_im = I_DC2 * alpha_DC1_sta

            I_DC3a = 2 * (tb_S) / (3 * rho_SS) * ((tb_S) ** 2 - 3 * (tb_S) * R + 3 * R ** 2) * (fm * w * alpha_DC1_dyn)
            I_DC3b = 2 * (tb_S) / (3 * rho_SS) * ((tb_S) ** 2 - 3 * (tb_S) * R + 3 * R ** 2) * (fm * w * alpha_DC1_dyn[idx_s3a])
            I_3 = [I_DC3a[:idx_s3a], I_DC3b[idx_s3a:]]
            I_3 = np.concatenate(I_3).ravel()
            I_3_im = I_3

            I_tot = (I_DC1 + I_DC2 + I_3)
            I_tot_im = (I_DC1_im + I_DC2_im + I_3_im)
            I_tot_re = (I_tot * alpha_DC1_sta * w * tau_DC1_sta)
            # I_tot_re = np.sqrt(I_tot ** 2 - I_tot_im ** 2)
            I_tot = (I_tot_re + 1j * I_tot_im)

            # fac = np.sqrt(w[idx_s1:]) / np.sqrt(w[idx_s1])
            # I_tot = [I_tot[:idx_s1], I_tot[idx_s1:] * fac]
            # I_tot = np.concatenate(I_tot).ravel()

            # Calculating the coupled loop equivalent parameter
            R_ap = P_tot / np.real((I_tot * np.conjugate(I_tot)))
            L_ap = tau_DC1_sta * R_ap[0]
            M_ap = (1j * w * L_ap * I_tot + I_tot * R_ap) / (1j * w * 1)
            # M_ap = np.sqrt(np.real(M_ap) ** 2 + np.imag(M_ap) ** 2)
            M_ap = np.transpose(np.ones(M_ap.shape).transpose() * M_ap[0])

            R_BS.append(R_ap)
            L_BS.append([L_ap[0]] * len(frequency))
            M_BS.append(M_ap)
            I_BS.append(I_tot)
            P_BS.append(P_tot)
            tau_BS.append(tau_DC1_sta)

        L_BS = np.array(L_BS).transpose()
        R_BS = np.array(R_BS).transpose()
        M_BS = np.array(M_BS).transpose()
        I_BS = np.array(I_BS).transpose()
        P_BS = np.array(P_BS).transpose()
        tau_BS = np.array(tau_BS).transpose()

        self.__setAttribute(self.BS, 'P', P_BS)
        self.__setAttribute(self.BS, 'I', I_BS)
        self.__setAttribute(self.BS, 'tau', tau_BS)
        self.__setAttribute(self.BS, 'L', L_BS)
        self.__setAttribute(self.BS, 'R', R_BS)
        self.__setAttribute(self.BS, 'M', M_BS)


    def calculate_Wedge(self, T: float):
        '''
        Function that calculates the equivalent parameter for eddy currents in the copper Wedge
        It takes the Temperature. It then calculates the resistivity and
        __interpolates the current and power from a pre-simulated Comsol model that includes the wedges effect.

        :param T: Temperature vector
        '''
        if not isinstance(self.Wedge.RRR_Wedge, (int, float)):
                raise Exception('Set flag_Wedge=True, but no RRR_Wedge provided.')
        rho_W = self.__rhoCu_nist(T=T, RRR=self.Wedge.RRR_Wedge, B=np.array([0]))
        P_tot, I_tot, tau_W, frequency = self.__interpolate(rho=rho_W, case='Wedge')

        w = 2 * np.pi * frequency
        P_tot = P_tot * self.General.magnet_length * 2

        # Calculating the coupled loop equivalent parameter
        # R_W = P_tot / I_tot ** 2
        R_W = P_tot / np.real((I_tot * np.conjugate(I_tot)))
        L_W = tau_W * R_W[0]
        L_W = np.repeat(L_W, len(R_W))
        M_W = (1j * w * L_W * I_tot + I_tot * R_W) / (1j * w * 1)
        # M_W = np.sqrt(np.real(M_W*np.conjugate(M_W))) # Checked: is the same as the line below
        # M_W = np.sqrt(np.real(M_W) ** 2 + np.imag(M_W) ** 2)
        # M_W1 = M_W[:tau_index]
        # M_W2 = np.transpose(np.ones(len(M_W)-tau_index).transpose() * M_W[tau_index])
        # M_W = np.concatenate((M_W1, M_W2))
        M_W = np.transpose(np.ones(M_W.shape).transpose() * M_W[0])

        self.__setAttribute(self.Wedge, 'P', P_tot)
        self.__setAttribute(self.Wedge, 'I', I_tot)
        self.__setAttribute(self.Wedge, 'tau', tau_W)
        self.__setAttribute(self.Wedge, 'L', L_W)
        self.__setAttribute(self.Wedge, 'R', R_W)
        self.__setAttribute(self.Wedge, 'M', M_W)


    def calculate_CPS(self):
        '''
        Function that calculates the equivalent parameter for eddy currents in the coil protection sheets.
        It takes the Temperature. It then calculates the resistivity and
        __interpolates the current and power from Comsol model that includes the ColdBore effect.
        '''

        P_tot, I_tot, tau_CPS, frequency = self.__interpolate(rho=self.CPS.rho_CPS, case='CPS')
        w = 2 * np.pi * frequency
        P_tot = P_tot * self.General.magnet_length * 2

        # Calculating the coupled loop equivalent parameter
        # R_W = P_tot / I_tot ** 2
        R_CPS = P_tot / np.real((I_tot * np.conjugate(I_tot)))
        L_CPS = tau_CPS * R_CPS[0]
        L_CPS = np.repeat(L_CPS, len(R_CPS))
        M_CPS = (1j * w * L_CPS * I_tot + I_tot * R_CPS) / (1j * w * 1)
        # M_W = np.sqrt(np.real(M_W*np.conjugate(M_W))) # Checked: is the same as the line below
        # M_W = np.sqrt(np.real(M_W) ** 2 + np.imag(M_W) ** 2)
        M_CPS = np.transpose(np.ones(M_CPS.shape).transpose() * M_CPS[0])

        self.__setAttribute(self.CPS, 'P', P_tot)
        self.__setAttribute(self.CPS, 'I', I_tot)
        self.__setAttribute(self.CPS, 'tau', tau_CPS)
        self.__setAttribute(self.CPS, 'L', L_CPS)
        self.__setAttribute(self.CPS, 'R', R_CPS)
        self.__setAttribute(self.CPS, 'M', M_CPS)


    def calculate_AlRing(self):
        '''
        Function that calculates the equivalent parameter for eddy currents in the coil protection sheets.
        It takes the Temperature. It then calculates the resistivity and
        __interpolates the current and power from Comsol model that includes the ColdBore effect.
        '''

        rho_AlRing = self.AlRing.rho_AlRing
        P_tot, I_tot, tau_AlRing, frequency = self.__interpolate(rho=rho_AlRing, case='AlRing')
        w = 2 * np.pi * frequency
        P_tot = P_tot * self.General.magnet_length * 2

        # Calculating the coupled loop equivalent parameter
        # R_W = P_tot / I_tot ** 2
        R_AlRing = P_tot / np.real((I_tot * np.conjugate(I_tot)))
        L_AlRing = tau_AlRing * R_AlRing[0]
        L_AlRing = np.repeat(L_AlRing, len(R_AlRing))
        M_AlRing = (1j * w * L_AlRing * I_tot + I_tot * R_AlRing) / (1j * w * 1)
        # M_W = np.sqrt(np.real(M_W*np.conjugate(M_W))) # Checked: is the same as the line below
        # M_W = np.sqrt(np.real(M_W) ** 2 + np.imag(M_W) ** 2)
        M_AlRing = np.transpose(np.ones(M_AlRing.shape).transpose() * M_AlRing[0])

        self.__setAttribute(self.AlRing, 'P', P_tot)
        self.__setAttribute(self.AlRing, 'I', I_tot)
        self.__setAttribute(self.AlRing, 'tau', tau_AlRing)
        self.__setAttribute(self.AlRing, 'L', L_AlRing)
        self.__setAttribute(self.AlRing, 'R', R_AlRing)
        self.__setAttribute(self.AlRing, 'M', M_AlRing)


    def __interpolate(self, rho: np.ndarray, case: str) -> np.ndarray:
        '''
        Helper function that takes a temperature, fits the respective resistivity to it and __interpolates from other resistivity values.

        :param case: name of the effect to select the excel file from (Wedge or CB)
        :param rho: resistivity of the Effect
        '''
        if not isinstance( rho, np.ndarray):
            rho = np.array([rho])

        name = self.General.magnet_name
        path = Path(self.General.local_library_path).resolve()
        # Takes the PowerLoss excel file corresponding to that effect
        df_P = pd.read_csv(os.path.join(path, 'TFM_input', f'{name}_PowerLoss_{case}_Interpolation.csv')).dropna(axis=1)
        # Takes the InducedCurrent excel file corresponding to that effect
        df_I = pd.read_csv(os.path.join(path, 'TFM_input', f'{name}_InducedCurrent_{case}_Interpolation.csv')).dropna(axis=1)
        frequency_P = df_P['f'].values[1:]
        frequency_I = df_I['f'].values[1:]

        if not np.allclose(frequency_P, frequency_I):
            raise Exception(f'Error in interpolation of {case}: Frequency for current and power are not equal.')
        else:
            frequency = frequency_P
        if len(frequency) != len(self.frequency):
            if self.verbose: print('Interpolation frequency is different. Adjusting internal frequency.')
            self.frequency = frequency
        elif not np.allclose(frequency, self.frequency):
            if self.verbose: print('Interpolation frequency is different. Adjusting internal frequency.')
            self.frequency = frequency

        # Takes all the possible resistivity values included in these files
        resistivities = np.array(df_P.iloc[0, 1:]).astype(float)
        order = np.argsort(resistivities)
        resistivities = resistivities[order]

        P_temp = np.zeros((len(frequency),))
        I_temp_real = np.zeros((len(frequency),))
        I_temp_imag = np.zeros((len(frequency),))

        # Performs interpolation between the desired resistivity value (rho[0]) and the resistivity values extracted from the file.
        # This is done to obtain accurate values of power loss and induced current corresponding to the desired resistivity.
        for i in range(len(frequency)):
            P_res = df_P.loc[df_P['f'] == frequency[i]].reset_index(drop=True).values[0][1:]
            P_res = P_res[order].astype(float)
            P_temp[i] = np.interp(rho[0], resistivities, P_res)
            I_res = df_I.loc[df_I['f'] == frequency[i]].reset_index(drop=True).values[0][1::2]
            I_res = I_res[order].astype(float)
            I_temp_real[i] = np.interp(rho[0], resistivities, I_res)
            I_res = df_I.loc[df_I['f'] == frequency[i]].reset_index(drop=True).values[0][2::2]
            I_res = I_res[order].astype(float)
            I_temp_imag[i] = np.interp(rho[0], resistivities, I_res)
        I_tot = I_temp_real + 1j * I_temp_imag
        #I_tot = np.real(np.sqrt(I_tot * np.conjugate(I_tot)))

        P_tot = P_temp
        # In order to calculate the tau, it calls the helper function
        # tau_index = __calculate_tau_index(P_tot=P_tot, frequency=frequency)
        tau =  self.__calculate_tau(P_tot=P_tot, frequency=frequency, effect=case)

        return P_tot, I_tot, tau, frequency


    ####################################################################################################################
    ############################################### MAIN FUNCTION TFM ###############################################

    def change_coupling_parameter(self):
        '''
        Main function of TFM_model. It changes the equivalent coupling loop parameters for the corresponding magnet using all the other functions.
        '''

        frequency = self.frequency
        groups = self.General.groups
        T = self.temperature
        f_rho_original = self.Strands.f_rho_effective
        f_mag_Roxie= self.Strands.f_mag_Roxie
        Mutual_dict = {}

        # Inter-Strands Coupling Currents
        if self.Options.flag_ISCC:
            f_mag_X_ISCC = self.Strands.f_mag_X_Roxie
            f_mag_Y_ISCC = self.Strands.f_mag_Y_Roxie
            M_ISCC, I_ISCC, f_mag_X_ISCC_return, f_mag_Y_ISCC_return = self.calculate_ISCC(frequency=frequency, T=T, fMag_X=f_mag_X_ISCC, fMag_Y=f_mag_Y_ISCC, flag_save=False)
            self.calculate_ISCC(frequency=frequency, T=T, fMag_X=f_mag_X_ISCC, fMag_Y=f_mag_Y_ISCC, flag_save=True)
            self.ISCC.M = self.__adjust_M_for_short(self.ISCC.M)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'ISCC', self.domain, self.f_characteristic,
                                                           self.frequency, self.ISCC.L, self.ISCC.R, self.ISCC.M, groups=groups,
                                             force_new_name=self.General.lib_path)

        # Persistent currents and magnetization
        if self.Options.flag_PC:
            self.__setAttribute(self.Strands, 'f_rho_effective', f_rho_original)
            self.calculate_PC(frequency=frequency, T=T, fMag=f_mag_Roxie, flag_coupling=False, flag_save=True)
            if self.Options.flag_ISCC: # calculates coupling between PC and ISCC
                f_mag_PC = np.maximum(f_mag_Roxie - np.sqrt(f_mag_X_ISCC_return ** 2 + f_mag_Y_ISCC_return ** 2), 1e-12)
                M_PC_ISCC, I_PC_ISCC = self.calculate_PC(frequency=frequency, T=T, fMag=f_mag_PC, flag_coupling=False, flag_save=False)
                Mutual_dict['M_PC_ISCC'] = M_PC_ISCC
                Mutual_dict['I_PC_ISCC'] = I_PC_ISCC
            # self.PC.M = self.__adjust_M_for_short(self.PC.M)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'PC', self.domain, self.f_characteristic,
                                                           self.frequency, self.PC.L, np.array([]), self.PC.M, groups=groups,force_new_name=self.General.lib_path)

        # Inter-Filament Coupling Currents
        if self.Options.flag_IFCC:
            self.__setAttribute(self.Strands, 'f_rho_effective', f_rho_original)#Change rho_eff to 0.6
            if self.Options.flag_ISCC: # calculates coupling between IFCC and ISCC
                f_mag_IFCC = np.maximum(f_mag_Roxie - np.sqrt(f_mag_X_ISCC_return ** 2 + f_mag_Y_ISCC_return ** 2), 1e-12)
                M_IFCC_ISCC, I_IFCC_ISCC = self.calculate_IFCC(frequency=frequency, T=T, fMag=f_mag_IFCC, flag_coupling=False, flag_save=False)
                Mutual_dict['M_IFCC_ISCC'] = M_IFCC_ISCC
                Mutual_dict['I_IFCC_ISCC'] = I_IFCC_ISCC
            if self.Options.flag_ED: # calculates coupling between IFCC and ED
                M_IFCC_ED, I_IFCC_ED = self.calculate_IFCC(frequency=frequency, T=T, fMag=f_mag_Roxie, flag_coupling=True, flag_save=False)
                Mutual_dict['M_IFCC_ED'] = M_IFCC_ED
                Mutual_dict['I_IFCC_ED'] = I_IFCC_ED
            self.calculate_IFCC(frequency=frequency, T=T, fMag=f_mag_Roxie, flag_coupling=False, flag_save=True)
            # M_IFCC = self.__adjust_M_for_short(self.IFCC.M)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'IFCC', self.domain, self.f_characteristic,
                                                           self.frequency, self.IFCC.L, self.IFCC.R, self.IFCC.M, groups=groups,force_new_name=self.General.lib_path)

        # Eddy currents in the copper sheath
        if self.Options.flag_ED:
            self.__setAttribute(self.Strands, 'f_rho_effective', f_rho_original)
            if self.Options.flag_ISCC: # calculates coupling between ED and ISCC
                f_mag_ED = np.maximum(f_mag_Roxie - np.sqrt(f_mag_X_ISCC_return ** 2 + f_mag_Y_ISCC_return ** 2), 1e-12)
                M_ED_ISCC, I_ED_ISCC = self.calculate_ED(frequency=frequency, T=T, fMag=f_mag_ED, flag_coupling=True, flag_save=False)
                Mutual_dict['M_ED_ISCC'] = M_ED_ISCC
                Mutual_dict['I_ED_ISCC'] = I_ED_ISCC

            self.calculate_ED(frequency=frequency, T=T, fMag=f_mag_Roxie, flag_coupling=False, flag_save=True)
            # M_ED = self.__adjust_M_for_short(self.ED.M)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'ED', self.domain, self.f_characteristic,
                                                           self.frequency, self.ED.L, self.ED.R, self.ED.M, groups=groups,
                                             force_new_name=self.General.lib_path)

        # Eddy currents in the Wedge
        if self.Options.flag_Wedge:
            self.calculate_Wedge(T=T)
            self.Wedge.M = self.__adjust_M_for_sections(self.Wedge.M, sum_type='aperture')
            # M_Wedge = self.__adjust_M_for_short(self.Wedge.M, flag_component=True)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'Wedge', self.domain, self.f_characteristic,
                                                            self.frequency, self.Wedge.L, self.Wedge.R, self.Wedge.M, groups=1,
                                                          force_new_name=self.General.lib_path)
            # Calculates coupling between Wedge and the conductor Losses effects
            M_W = self.__calculate_Coupling_Components(Effect='Wedge')
            Mutual_dict.update(M_W)

        # Eddy currents in the Cold Bore
        if self.Options.flag_CB:
            self.calculate_CB(T=T)
            self.CB.M = self.__adjust_M_for_sections(self.CB.M, sum_type='aperture')
            # M_CB = self.__adjust_M_for_short(self.CB.M, flag_component=True)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'CB', self.domain, self.f_characteristic,
                                                           self.frequency, self.CB.L, self.CB.R, self.CB.M, groups=1,
                                                          force_new_name=self.General.lib_path)
            # Calculates coupling between CB and the conductor Losses effects
            M_CB = self.__calculate_Coupling_Components(Effect='CB')
            Mutual_dict.update(M_CB)

        # Eddy currents in the Coil Protection Sheets
        if self.Options.flag_CPS:
            self.calculate_CPS()
            self.CPS.M = self.__adjust_M_for_sections(self.CPS.M, sum_type='aperture')
            # M_CPS = self.__adjust_M_for_short(self.CPS.M, flag_component=True)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'CPS', self.domain, self.f_characteristic,
                                                           self.frequency,  self.CPS.L,
                                                          self.CPS.R, self.CPS.M, groups= 1,
                                                          force_new_name=self.General.lib_path)
            # Calculates coupling between CPS and the conductor Losses effects
            if isinstance(self.CPS.group_CPS, (int, float)):
                field_int_value= self.CPS.group_CPS
            else:
                field_int_value = self.temperature

            M_CPS = self.__calculate_Coupling_Components(Effect='CPS', field_int_value=field_int_value)
            Mutual_dict.update(M_CPS)

        # Eddy currents in the Aluminum ring
        if self.Options.flag_AlRing:
            self.calculate_AlRing()
            self.AlRing.M = self.__adjust_M_for_sections(self.AlRing.M, sum_type='aperture')
            # M_AlRing = self.__adjust_M_for_short(self.AlRing.M, flag_component=True)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'AlRing', self.domain, self.f_characteristic,
                                                           self.frequency, self.AlRing.L,
                                                          self.AlRing.R, self.AlRing.M, groups=1,
                                                          force_new_name=self.General.lib_path)
            # Calculates coupling between AlRing and the conductor Losses effects
            M_AlRing = self.__calculate_Coupling_Components(Effect='AlRing')
            Mutual_dict.update(M_AlRing)

        # Eddy currents in the beam screen
        if self.Options.flag_BS:
            self.calculate_BS()
            self.BS.M = self.__adjust_M_for_sections(self.BS.M, sum_type='aperture')
            # M_BS = self.__adjust_M_for_short(self.BS.M, flag_component=True)
            self.General.lib_path = change_library_EqLoop(self.General.lib_path, 'BS', self.domain, self.f_characteristic,
                                                          self.frequency, self.BS.L,
                                                              self.BS.R, self.BS.M, groups=2,
                                                              force_new_name=self.General.lib_path)
            # Calculates coupling between AlRing and the conductor Losses effects
            M_BS = self.__calculate_Coupling_Components(Effect='BS')
            Mutual_dict.update(M_BS)

        # Calculates mutual coupling coefficients using the Mutual_dict values
        if len(Mutual_dict) != 0:
            self.__calculate_Mutual_Coupling(Mutual_dict)

        if self.Options.flag_PC and self.Options.flag_IFCC: # Changes values of M_PC_IFCC in the .lib file
            M_PC_IFCC = -1 * np.repeat(self.PC.M_PC_IFCC, np.sum(self.HalfTurns.n_strands))
            for i in range(1,groups+1):
                self.General.lib_path = change_library_MutualCoupling(self.General.lib_path, f'M_PC_IFCC_{i}', frequency, M_PC_IFCC)
        if self.Options.flag_PC and self.Options.flag_ED:  # calculates coupling between PC and ED
            M_PC_ED =-1 * np.repeat(self.PC.M_PC_IFCC, np.sum(self.HalfTurns.n_strands))
            for i in range(1, groups + 1):
                self.General.lib_path = change_library_MutualCoupling(self.General.lib_path, f'M_PC_ED_{i}', frequency, M_PC_ED)

        if self.magnet_data.magnet_Couplings is not None:
            for key, value in self.magnet_data.magnet_Couplings.__dict__.items():
                if 'M_' not in key or value is None: continue
                first_effect = key.split('_')[-2]  # Taking the name of the first effect
                second_effect = key.split('_')[-1]
                if not self.__getAttribute('Options', f'flag_{first_effect}') or not self.__getAttribute('Options', f'flag_{second_effect}'): continue
                if isinstance(value, np.ndarray):
                    M_value = np.repeat(value, len(frequency))
                else:
                    M_value = np.array([value] * len(frequency))
                self.General.lib_path = change_library_MutualCoupling(self.General.lib_path, key, frequency, M_value)

                if self.flag_debug:
                    fig_path = os.path.abspath(os.path.join(self.output_path, '..'))
                    fig_path = os.path.join(fig_path, 'plots_Debug')
                    os.makedirs(fig_path, exist_ok=True)

                    list_legend = []
                    cases = [key, f'K_{first_effect}_{second_effect}']
                    fig, ax1 = plt.subplots()
                    ax2 = ax1.twinx()
                    for case in cases:
                        if case == key:
                            ax1.semilogx(frequency, np.real(M_value), color='tab:orange', marker='*')
                            list_legend.append(f'Re({key})')
                            ax1.semilogx(frequency, np.imag(M_value), color='tab:olive', marker='s')
                            list_legend.append(f'Im({key})')
                        else:
                            L1 = self.__getAttribute(first_effect, 'L')
                            L2 = self.__getAttribute(second_effect, 'L')
                            k_value = M_value / np.sqrt(L1 * L2.T)
                            if len(k_value.shape)>1:
                                if k_value.shape[1]>k_value.shape[0]:
                                    k_value = k_value.T
                            ax2.semilogx(frequency, np.real(k_value), color='tab:brown', marker='*')
                            list_legend.append(f'Re({case})')
                            ax2.semilogx(frequency, np.imag(k_value), color='tab:pink', marker='s')
                            list_legend.append(f'Im({case})')
                    ax1.grid(True)
                    ax1.legend(list_legend, loc='upper left')
                    ax1.set_xlabel('Frequency [Hz]')
                    ax2.set_ylabel(f'{case} [-]')
                    ax1.set_ylabel(f'{case} [H]')
                    ax1.set_title(f'{case} plot for different groups - {self.General.magnet_name}', fontweight='bold')
                    fig_path_final = os.path.join(fig_path, f'{first_effect}_{second_effect}_plot.png')
                    plt.savefig(fig_path_final)
                    plt.close()

        # _ = self.check_inductance_matrix_losses(Mutual_dict)


        if self.flag_debug:
            fig_path = os.path.abspath(os.path.join(self.output_path, '..'))
            fig_path = os.path.join(fig_path, 'plots_Debug')
            os.makedirs(fig_path, exist_ok=True)

            for eff, value in self.effects.items():
                if value:
                    fig, axes = plt.subplots(3, 3, figsize=(26, 18))

                    attributes = ['I', 'P', 'L', 'R', 'M' , 'K']
                    y_labels = ['I [A]', 'P [W]', 'L [H]', 'R [ohm]', 'M [H]', 'k [-]']
                    ax_count = 0
                    for attr, y_label in zip(attributes, y_labels):
                        ax = axes.flatten()[ax_count]
                        ax_count += 1
                        if attr == 'R' and eff == 'PC': continue
                        if attr == 'P' and eff == 'PC': continue
                        if attr != 'K':
                            data = self.__getAttribute(eff, attr)
                        else:
                            M = self.__getAttribute(eff, 'M')
                            L = self.__getAttribute(eff, 'L')
                            if len(M.shape)>1:
                                if M.shape == np.sqrt(L * self.General.L_mag / 2).shape:
                                    data = M / np.sqrt(L * self.General.L_mag / 2)
                                else:
                                    try:
                                        data = M.T / np.sqrt(L * self.General.L_mag / 2)
                                    except:
                                        pass
                            else:
                                data = M / np.sqrt(L * self.General.L_mag / 2)
                        lns = []
                        if len(data.shape)==1:
                            data = data[:,np.newaxis].T
                        if data.shape[0] != len(frequency):
                            data = data.T
                        for i in range(data.shape[1]):
                            if attr == 'M' or attr=='K':
                                lns1 = ax.semilogx(frequency, np.real(data[:, i]), marker='*', label=f'Group {i + 1}, Re({attr})')
                                lns2 =  ax.semilogx(frequency, np.imag(data[:, i]), marker='s', label=f'Group {i + 1}, Im({attr})')
                                lns = lns + lns1 + lns2
                            else:
                                lns += ax.semilogx(frequency, data[:, i], marker='*', label=f'Group {i+1}')
                        ax.grid(True)
                        labs = [l.get_label() for l in lns]
                        ax.legend(lns, labs, loc=0)
                        ax.set_xlabel('Frequency [Hz]')
                        ax.set_ylabel(y_label)
                    plt.title(f'{eff} plot - {self.General.magnet_name}', fontweight='bold')
                    fig_path_final = os.path.join(fig_path, f'{eff}_plot.png')
                    plt.savefig(fig_path_final)
                    plt.close()


    ####################################################################################################################
    ############################################### MUTUAL COUPLING CALCULATION #########################################
    def __adjust_M_for_sections(self, M_total: np.ndarray, sum_type: str = 'aperture'):
        '''
        Helper function that splits the mutual inductance of a component into its respective section

        :param M_total : it contains the total mutual coupling associated with an effect
        :param sum_type: can either be 'aperture' or 'full' and indicates how to split the mutual coupling
        '''
        if not sum_type.lower() in ['aperture','full']:
            raise Exception(f'Do not understand how to split the mutual coupling. Available: aperture, full')

        sections_to_apertures = self.General.sections_to_apertures
        sections = len(sections_to_apertures)

        if len(M_total.shape)==1:
            M_total = np.repeat(M_total[:,np.newaxis],2, axis=1)

        M_adj = np.zeros((sections,M_total.shape[0])).astype(np.complex_)

        L_ap = np.zeros((self.General.apertures,))
        for ap in range(1,self.General.apertures+1):
            L_ap[ap-1] = np.sum(self.General.inductance_to_section[np.where(sections_to_apertures==ap)[0]])

        fL_sections = np.zeros((sections, ))
        for n in range(1,sections+1):
            ap = sections_to_apertures[n-1]
            fL_section = np.sum(self.General.inductance_to_section[n-1])/(L_ap[ap-1])
            fL_sections[n-1] = fL_section
            M_adj[n-1,:] = M_total[:,ap-1]*fL_section

        if self.Shorts.sections_to_short:
            M_adj = self.__adjust_M_for_short(M_adj, flag_component=True)

        return M_adj.T


    def __adjust_M_for_short(self, M_adj: np.ndarray, flag_component: bool = False, flag_1D: bool = False):
        '''
            Helper function that adjusts the mutual inductance of a component by taking into account the presence of shorts.

            :param M_adj : array that contains the mutual coupling to be adjusted
            :param flag_component: if not the approach used is the one with V across coil
        '''
        if self.Shorts.sections_to_short:
            R_short = self.Shorts.short_resistances[0]
            sections = np.array(self.Shorts.sections_to_short[0].split('-')).astype(int)
            sections_not_shorted = np.delete((np.arange(self.General.groups)+1), sections-1)
            L_shorted = np.sum(self.General.inductance_to_section[sections-1])

            ###############################
            ## Approach with V across coil
            Z_0, Z_total = self.__calculate_Ztotal()
            f_new = abs(Z_total/Z_0)

            x = 1

            if not flag_component:
                M_adj[:, sections - 1] = np.transpose(M_adj[:, sections - 1].T * (1-f_new))
            else:
                M_adj[sections - 1, :] = M_adj[sections - 1, :] * 1

        return M_adj


    def __calculate_Ztotal(self):
        '''

        :return:
        :rtype:
        '''
        w = 2 * np.pi * self.frequency
        R_short = self.Shorts.short_resistances[0]
        sections = np.array(self.Shorts.sections_to_short[0].split('-')).astype(int)
        sections_not_shorted = np.delete((np.arange(self.General.groups) + 1), sections - 1)
        L_shorted = np.sum(self.General.inductance_to_section[sections - 1])
        ap = np.unique(self.General.sections_to_apertures[sections - 1])[0]
        idx = np.where(self.General.sections_to_apertures == ap)[0]

        M_matrix = np.zeros_like(self.General.inductance_to_section)
        M_matrix[np.ix_(idx, idx)] = self.General.inductance_to_section[np.ix_(idx, idx)]
        L_shorted = np.sum(np.diag(M_matrix)[sections - 1])

        Z_0 = (1j * w * np.sum(M_matrix))

        s = 1j * w
        lower_triangular_mask = np.tril(np.ones(M_matrix.shape, dtype=bool), k=-1)
        Z1a = -s * L_shorted * np.sum(np.diag(M_matrix)[sections_not_shorted - 1])
        Z2a = R_short * np.sum(np.diag(M_matrix))
        Z3a = s * np.sum(np.delete(M_matrix[sections - 1], sections - 1) ** 2)
        Z4a = 2 * R_short * np.sum(M_matrix[lower_triangular_mask])

        row = np.delete(M_matrix[sections - 1], sections - 1)
        Mprod = 0
        for i in range(len(row) - 1):
            for j in range(i + 1, len(row)):
                Mprod += row[i] * row[j]
        Z5a = 2 * s * Mprod
        ltm = copy.deepcopy(lower_triangular_mask)
        ltm[sections - 1, :] = False
        ltm[:, sections - 1] = False
        Z6a = - 2 * L_shorted * s * np.sum(M_matrix[ltm])
        Z_b = s / (s * L_shorted - R_short)

        Z_total = Z_b * (Z1a + Z2a + Z3a + Z4a + Z5a + Z6a)
        return Z_0, Z_total


    def __calculate_Mutual_Coupling(self, Mutual_dict: dict):
        '''
        This function calculates the Mutual Coupling coefficients between two different effects and inserts this value
        in the corresponding .FUNC of the lib file

        : param Mutual_dict: dictionary containing all the Mutual Coupling values between the effects
        '''
        frequency = self.frequency
        w = 2*np.pi*frequency
        groups = self.General.groups
        sections_to_apertures = self.General.sections_to_apertures
        
        for key, value in Mutual_dict.items(): # example of key = M_IFCC_ISCC
            if key.startswith('I'): continue
            first_effect = key.split('_')[-2] # Taking the name of the first effect
            second_effect = key.split('_')[-1]  # Taking the name of the second effect
            # if second_effect in self.effs_notCond: continue
            if first_effect == 'ISCC':
                sort_on = 'halfturns'
            else:
                sort_on = 'strands'
            M_first_effect = self.__getAttribute(first_effect, f'M_{sort_on}') # Taking the value of M not coupled corresponding to the first effect and saved in the dataclass
            I_second_effect = self.__getAttribute(second_effect, 'I')  # Taking the value of I corresponding to the sceond effect and saved in the dataclass
            M_key = key
            I_value = Mutual_dict[f'I_{first_effect}_{second_effect}']

            if self.flag_debug:
                fig_path = os.path.abspath(os.path.join(self.output_path, '..'))
                fig_path = os.path.join(fig_path, 'plots_Debug')
                os.makedirs(fig_path, exist_ok=True)

                lns = []
                # cases = [M_key, f'K_{first_effect}_{second_effect}']
                cases = [f'K_{first_effect}_{second_effect}']
                fig, ax1 = plt.subplots()
                ax2 = ax1.twinx()

            for ap in range(1,self.General.apertures+1):
                for i in range(1,groups+1):
                    if first_effect == 'ISCC':
                        idx_group = np.where(self.HalfTurns.HalfTurns_to_sections==i)[0]
                    else:
                        idx_group = np.where(self.Strands.strands_to_sections == i)[0]
                    M_val = value[:,idx_group]
                    I_val = I_value[:, idx_group]
                    if sections_to_apertures[i-1]!=ap: continue
                    M_first = M_first_effect[:,idx_group]
                    if second_effect in self.effs_notCond:
                        if len(I_second_effect.shape)>1:
                            I_second = I_second_effect[:,ap-1]
                        else:
                            I_second = I_second_effect
                    else:
                        I_second = I_second_effect[:, i-1]

                    if first_effect != 'PC' and second_effect != 'PC':
                        R_first = self.__getAttribute(first_effect, f'R_{sort_on}')[:,idx_group]
                        I_first_strand = self.__getAttribute(first_effect, f'I_{sort_on}')[:,idx_group]
                        I_first = self.__getAttribute(first_effect, f'I')[:, i-1]
                    else:
                        R_first = np.zeros(M_first.shape)
                        I_first = 1
                        I_first_strand = np.ones(M_first.shape)


                    M_value = ((1/(1j*w*I_second * M_val.T)) *((1j*w*1)*(M_first ** 2 - M_val ** 2).T + (R_first*(I_first_strand*M_first - I_val*M_val)).T)).T
                    for p in range(M_value.shape[1]):
                        M_value[:,p] = interpolate_curve(M_value[:,p])
                    M_value = np.sum(M_value, axis=1)/len(M_value)

                    if first_effect == 'PC' or second_effect == 'PC':
                        M_value = -1 * M_value

                    self.General.lib_path = change_library_MutualCoupling(self.General.lib_path, f'{M_key}_{i}', frequency, M_value)

                    if self.flag_debug:
                        for case in cases:
                            if case == M_key:
                                lns1 = ax1.semilogx(frequency, np.real(M_value), marker='*', label=f'Re({M_key})')
                                lns2 = ax1.semilogx(frequency, np.imag(M_value), marker='s', label=f'Im({M_key})')
                                lns = lns + lns1 + lns2
                            else:
                                L1 = self.__getAttribute(first_effect, 'L')
                                if len(L1.shape) > 1:
                                    if L1.shape[1] == groups: L1 = L1[:, i - 1]
                                    else: L1 = L1[:, ap - 1]
                                L2 = self.__getAttribute(second_effect, 'L')
                                if len(L2.shape)>1:
                                    if L2.shape[1]==groups: L2 = L2[:,i-1]
                                    else: L2 = L2[:,ap-1]
                                k_value = M_value / np.sqrt(L1 * L2)
                                # if np.any(k_value>1):
                                #     xxx = 1
                                lns1 = ax2.semilogx(frequency, np.real(k_value), marker='*', label=f'Re({case})')
                                lns2 = ax2.semilogx(frequency, np.imag(k_value), marker='s', label=f'Im({case})')
                                lns = lns + lns1 + lns2
            if self.flag_debug:
                labs = [l.get_label() for l in lns]
                ax1.legend(lns, labs, loc=0)
                ax1.set_xlabel('Frequency [Hz]')
                ax2.set_ylabel(f'{case} [-]')
                # ax2.set_ylim([-1,1])
                ax1.set_ylabel(f'{case} [H]')
                ax1.set_title(f'{case} plot for group {i} - {self.General.magnet_name}', fontweight='bold')
                ax1.grid(True)
                fig_path_final = os.path.join(fig_path, f'{first_effect}_{second_effect}_plot.png')
                plt.savefig(fig_path_final)
                plt.close()


    def __calculate_Coupling_Components(self, Effect: str, field_int_value: float = None) -> dict:
        '''
        This function calculates the Mutual Coupling values between the conductor losses and the given Effect

        :param Effect: str that indicates the corresponding Not Conductor Loss effect -> Wedge or CB

        :return M_dict: dictionary with the name of the Mutual coupling and the values
        '''
        M_dict = {}

        # Retrieve f_mag, f_mag_X and f_mag_Y from the Comsol field files specific for each effect
        f_mag, f_mag_X, f_mag_Y = self.__read_COMSOL_field_file(Effect, field_int_value= field_int_value)
        frequency = self.frequency
        T = self.temperature

        effs = self.effects
        effs_NotCond = self.effs_notCond   # Taking only the effects not corresponding to the conductor losses
        for eff, value in effs.items():
            if eff in effs_NotCond: continue
            if value == True:  # If the flag of an effect is set takes the name of the effect
                # Calls the calculate function of the corresponding effect and calculates the M
                if eff == 'ISCC':  # attributes -> fMag_X, fMag_Y
                    M, I, _, _ = getattr(self, f'calculate_{eff}')(frequency=frequency, T=T, fMag_X=f_mag_X, fMag_Y=f_mag_Y, flag_save=False)
                else: # attributes -> fMag
                    M, I = getattr(self, f'calculate_{eff}')(frequency=frequency, T=T, fMag=f_mag, flag_coupling=True, flag_save=False)

                M_dict[f'M_{eff}_{Effect}'] = M # Save the new M in the dictionary
                M_dict[f'I_{eff}_{Effect}'] = I  # Save the new I in the dictionary

        return M_dict


    ####################################################################################################################
    ############################################ FUNCTION TO CALCULATE THE GROUPING #####################################
    def __group_components(self, frequency: np.ndarray, L: np.ndarray, R: np.ndarray, M: np.ndarray, sort_on: str = 'strands', I: np.ndarray = np.array([])) -> np.ndarray:
        '''
        Helper function that groups components into n groups, based on a sorting on a specific variable out of R,L,M

        :param frequency: frequency vector
        :param L: L-vector
        :param R: R-vector
        :param M: M_vector
        :param groups: number of groups to be separated
        :param sort_on: Which variable to sort on
        :return: 3 np.ndarray in the order: L,R,M that are groupned into n_groups
        '''

        avail_sort = ['strands', 'halfturns']#, 'turns', 'apertures']
        sort_on = sort_on.lower()
        if sort_on not in avail_sort:
            raise Exception(f'Do not understand the sorting argument. Available: {avail_sort}')
        groups = self.General.groups

        # Decide on the grouping
        if sort_on == 'strands':
            x = self.Strands.strands_to_sections
        elif sort_on == 'halfturns':
            x = self.HalfTurns.HalfTurns_to_sections

        f = frequency
        R_group = np.zeros((len(f), groups), dtype=float)
        M_group = np.zeros((len(f), groups), dtype=np.complex_)
        L_group = np.zeros((len(f), groups), dtype=float)
        I_group = np.zeros((len(f), groups), dtype=np.complex_)

        # Loop through the resistivities

        for i in range(1, groups + 1):
            group_indexes = np.where(x == i)[0]

            if len(group_indexes) > 0:
                for j in range(len(f)):
                    # group the resistivities and take the mean of their M
                    R_temp = np.nan_to_num(R[j, :]).astype(float)
                    M_temp = np.nan_to_num(M[j, :]).astype(complex)
                    L_temp = np.nan_to_num(L[j, :]).astype(float)
                    I_temp = np.nan_to_num(I[j, :]).astype(complex) if len(I) != 0 else None

                    R_group[j, i - 1] = np.mean(R_temp[group_indexes])
                    L_group[j, i - 1] = np.mean(L_temp[group_indexes])

                    if I_temp is not None:
                        I_group[j, i - 1] = np.sum(M_temp[group_indexes] * I_temp[group_indexes])

                    # M_sel = np.sum(M_temp[group_indexes] ** 2)
                    # s_r_temp = np.sign(np.real(M_sel))
                    # s_i_temp = np.sign(np.imag(M_sel))
                    # M_group[j, i - 1] = s_r_temp * np.real(np.sqrt(M_sel)) + 1j * s_i_temp * np.imag(np.sqrt(M_sel))
                    M_group[j, i - 1] = np.sqrt(np.sum(M_temp[group_indexes] ** 2))
            M_group[:, i - 1] = check_smoothness(frequency, np.real(M_group[:, i - 1])) + 1j * check_smoothness(frequency, np.imag(M_group[:, i - 1]))

        # Optionally, you can filter out rows with all zeros afterward if needed
        R_group = R_group[np.any(R_group != 0, axis=1)]
        M_group = M_group[np.any(M_group != 0, axis=1)]
        L_group = L_group[np.any(L_group != 0, axis=1)]

        if len(I) != 0:
            I_group = I_group / M_group
            return L_group, R_group, M_group, I_group
        else:
            return L_group, R_group, M_group


    def __group_mutual_coupling(self, M: np.ndarray) -> np.ndarray:
        '''
        Helper function that groups components into n groups, based on a sorting on a specific variable out of R,L,M

        :param M: M_vector

        :return: 1 np.ndarray: M that are grouped into n_groups
        '''
        frequency = self.frequency
        groups = self.General.groups
        M_group = np.zeros((len(frequency), ), dtype=np.complex_)
        M_group_t = np.zeros((len(frequency),), dtype=np.complex_)
        x = self.Strands.strands_to_sections

        # Loop through the frequencies
        for j in range(len(frequency)):
            M_temp = np.nan_to_num(M[j, :]).astype(complex)
            if len(M_temp) > 0:
                # M_sel = np.sum(M_temp ** 2)
                # s_r_temp = np.sign(np.real(M_sel))
                # s_i_temp = np.sign(np.imag(M_sel))
                # M_group_t[j] = s_r_temp * np.real(np.sqrt(M_sel)) + 1j * s_i_temp * np.imag(np.sqrt(M_sel))
                M_group[j] = np.sqrt(np.sum(M_temp ** 2))
        M_group = check_smoothness(frequency, np.real(M_group))+1j*check_smoothness(frequency, np.imag(M_group))

        return M_group


    ####################################################################################################################
    ############################################ FUNCTIONS FOR L MATRX CHECKING #####################################
    def check_inductance_matrix_losses(self, Mutual_dict: dict):
        '''
        This function constructs the L Matrix containing all the effects that are selected.
        This function has in the diagonal all the L corresponding to a given effect
        On the first column and on the first row at the index corresponding to that effect it has the M of that effect
        In the crossing betwwen indices of different effects, it has the mutual coupling between these two.
        In all the other places it has 0

        :param Mutual_dict: dictionary with the Mutual coupling between all the different effects
        '''
        frequency = self.frequency
        groups = self.General.groups
        effs = list(self.effects.keys())

        effects = np.repeat(np.array(effs), groups)
        effects = np.insert(effects, 0, 'Mag').astype(str)
        L_matrix_list = []

        for freq in range(len(frequency)):
            # Creating the matrix and filling it with 0
            L_matrix = np.zeros((len(effects), len(effects))).astype(complex)
            for eff in range(len(effects)):
                if effects[eff]!='Mag' and self.effects[effects[eff]]:
                    if eff == 0:  # Checking if the Effect[eff] == 'Mag'
                        L_matrix[0, 0] = self.General.L_mag
                    else:
                        if effects[eff-1] == effects[eff]: # Checking if it's not the first time that we encounter this effect in the dict
                            count_group += 1  # If it's not the first time, the group counting must be incremented
                        else:
                            count_group = 0  # If it is the first time, the group counting is set to zero

                        # Filling the matrix with the L values along the diagonal and the M values symmetrically
                        # on the first row and on the first column, selecting the right values according to count_group
                        if effects[eff] in self.effs_notCond and effects[eff] != 'BS':
                            L_matrix[0, eff] = self.__getAttribute(effects[eff], 'M')[freq]
                            L_matrix[eff, 0] = self.__getAttribute(effects[eff], 'M')[freq]
                            L_matrix[eff, eff] = self.__getAttribute(effects[eff], 'L')[freq]
                        else:
                            L_matrix[0, eff] = self.__getAttribute(effects[eff], 'M')[freq, count_group]
                            L_matrix[eff, 0] = self.__getAttribute(effects[eff], 'M')[freq, count_group]
                            L_matrix[eff, eff] = self.__getAttribute(effects[eff], 'L')[freq, count_group]

                        for key, value in Mutual_dict.items():
                            if effects[eff] in key:  # For each key of the dict, check if the current effect is contained in it
                                for l in range(len(effects)):  # If yes, find the other effect contained in the same key
                                    if l != 0 and eff != l and effects[l] in key:
                                        if effects[l - 1] != effects[l]:
                                            # Take the first effect with that name and then select the right column index
                                            # and the right value by selecting the same count_group of the effects[eff] element
                                            L_matrix[eff, l+count_group] = value[freq, count_group]
                else: 
                    continue
            L_matrix_list.append(L_matrix)

        for i in range(len(L_matrix_list)):
            if not is_positive_definite(L_matrix_list[i]):
                # raise Exception(f'Matrix not positive definite for frequency {frequency[i]}')
                print(f'Matrix not positive definite for frequency {frequency[i]}')
        return 1


    ########################################################################################################################
    ################################## FUNCTION TO CALCULATE TAU OF COMPONENTS  ########################################
    def __calculate_tau(self, P_tot: np.ndarray, frequency: np.ndarray, effect: str) -> int:
        '''
        Helper function to calculate the tau_index corresponding to the frequency vector for a specific effect

        :param P_tot: P vector used to calculate the tau

        :return: tau_index corresponding to the frequency vector
        '''

        def central_difference_log(x_values, f_values):
            h_forward = x_values[1:] - x_values[:-1]  # Spacing between successive points
            h_backward = x_values[1:] - x_values[:-1]

            derivative = np.zeros_like(f_values)
            # Central difference for interior points
            for i in range(1, len(x_values) - 1):
                h = (x_values[i + 1] - x_values[i - 1]) / 2
                derivative[i] = (f_values[i + 1] - f_values[i - 1]) / (2 * h)

            # Forward difference for the first point
            derivative[0] = (f_values[1] - f_values[0]) / h_forward[0]

            # Backward difference for the last point
            derivative[-1] = (f_values[-1] - f_values[-2]) / h_backward[-1]

            return derivative

        def split_consecutive(arr):
            # Initialize the list to hold subarrays and the first subarray
            result = []
            subarray = [arr[0]]
            # Iterate through the array starting from the second element
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    # If current element is consecutive, add it to the current subarray
                    subarray.append(arr[i])
                else:
                    # If current element is not consecutive, add the current subarray to result
                    result.append(subarray)
                    # Start a new subarray
                    subarray = [arr[i]]
            # Add the last subarray to the result
            result.append(subarray)

            return result

        frequencies_tau = np.logspace(np.log10(frequency[0]), np.log10(frequency[-1]), 1000)
        Pt = np.interp(frequencies_tau, frequency, P_tot)
        dPt = smooth_curve(central_difference_log(frequencies_tau, Pt), 21, n_pad=5)
        dPt2 = smooth_curve(central_difference_log(frequencies_tau, dPt), 21, n_pad=5)

        if frequencies_tau[np.argmin(dPt2)] < 10:
            min_tol = 1e-6
            tol = min(10 ** (np.round(np.log10(dPt2.max()), 0) - 3), min_tol)
        elif frequencies_tau[np.argmin(dPt2)] < 100:
            if effect == 'AlRing':
                tol = 3e-6
            elif effect == 'Wedge':
                tol = 1e-7
        else:
            min_tol = 1e-7
            tol = min(10 ** (np.round(np.log10(dPt2.max()), 0) - 2), min_tol)

        split_array = split_consecutive(np.where(abs(dPt2) < tol)[0])
        if len(split_array) == 3:
            idx_tau = split_consecutive(np.where(abs(dPt2) < tol)[0])[-2][0]
        else:
            idx_tau = split_consecutive(np.where(abs(dPt2) < tol)[0])[-1][0]
        tau = 1 / frequencies_tau[idx_tau]

        return tau


    ####################################################################################################################
    ############################################ RESISTIVITY FUNCTIONS CALCULATION #####################################
    def __rhoCu_nist(self, T: float, RRR: np.ndarray, B: np.ndarray) -> np.ndarray:
        '''
        Helper function to calculate resistivity of copper. Taken from steam-materials library

        :param T: Temperature
        :return: array of resistivities
        '''
        B = abs(B)
        T_ref_RRR = 273
        # Make T of the same size of B and RRR
        T_flatten = np.tile(T, (len(B), 1)).flatten()
        # Create numpy2d by stacking B, RRR, and T along axis 0
        numpy2d = np.vstack((T_flatten, B, RRR, T_ref_RRR * np.ones_like(T_flatten)))
        sm_cp_rho = STEAM_materials('CFUN_rhoCu_v1', numpy2d.shape[0], numpy2d.shape[1])
        RhoCu = sm_cp_rho.evaluate(numpy2d)

        return RhoCu


    def __rhoSS_nist(self, T: float) -> np.ndarray:
        '''
        Helper function to calculate resistivity of copper. Taken from steam-materials library

        :param T: Temperature
        :return: array of resistivities
        '''
        T_flatten = np.tile(T, (1)).flatten()
        # Create numpy2d by stacking B, RRR, and T along axis 0
        sm_cp_rho = STEAM_materials('CFUN_rhoSS_v1', 1, 1)
        RhoSS = sm_cp_rho.evaluate(T_flatten)

        return RhoSS


    def __rhoAl_nist(self, T: float) -> np.ndarray:
        '''
        Helper function to calculate resistivity of copper. Taken from steam-materials library

        :param T: Temperature
        :return: array of resistivities
        '''
        T_flatten = np.tile(T, (1)).flatten()
        # Create numpy2d by stacking B, RRR, and T along axis 0
        sm_cp_rho = STEAM_materials('CFUN_rhoAl_v1', 1, 1)
        RhoAl = sm_cp_rho.evaluate(T_flatten)

        return RhoAl


    ####################################################################################################################
    ###################################### GET AND SET FUNCTIONS FOR THE ATTRIBUTES #####################################
    def __setAttribute(self, TFMclass, attribute: str, value):
        try:
            setattr(TFMclass, attribute, value)
        except:
            setattr(getattr(self, TFMclass), attribute, value)


    def __getAttribute(self, TFMclass, attribute: str):
        try:
            return getattr(TFMclass, attribute)
        except:
            try:
                return getattr(getattr(self, TFMclass), attribute)
            except:
                getattr(self, attribute)


########################################################################################################################
########################################################################################################################
########################################################################################################################

########################################################################################################################
############################### FUNCTIONS TO CHANGE .FUNC PARAMETERS IN THE LIB FILE  ###################################
def change_library_EqLoop(path_file: Path, element: str, domain: str, f_characteristic: float, frequency: np.ndarray, L_eq: np.ndarray, R_eq: np.ndarray, M_eq: np.ndarray, groups: int = 2, force_new_name: Path = ''):
    '''
    Helper function that changes the TFM magnet .lib file and includes in Table function the given R,L,M parameter

    element = Element, for which the RLM to be inserted e.g. BS, CPS, ED ...

    If L_eq, M_eq or R_eq are empty, they will not be written
    '''
    if groups==1:
        if L_eq.size: L_eq = L_eq.reshape((len(L_eq), 1))
        if R_eq.size: R_eq = R_eq.reshape((len(R_eq), 1))
        if not len(M_eq.shape)>1:
            M_eq = M_eq.reshape((len(M_eq), 1))

    if domain=='frequency':
        tab_stub = '{TABLE{FREQ}='
    else:
        tab_stub = '{TABLE{' + str(np.round(f_characteristic,2)) + '}='

    #### Creating string for equivalent inductance
    str_L = []
    if L_eq.size:
        for i in range(groups):
            group = [f'{element}_L_{i+1}(1)', tab_stub]
            str_group_L = f'.FUNC' + ' ' + ' '.join("{:<20}".format(g) for g in group)
            L = L_eq[:,i]
            for j in range(len(frequency)):
                str_group_L = str_group_L + f'({frequency[j]},{L[j]})     '
            str_group_L = str_group_L + '}\n'
            str_L.append(str_group_L)

    #### Creating string for equivalent resistance
    str_R = []
    if R_eq.size:
        for i in range(groups):
            group = [f'{element}_R_{i + 1}(1)', tab_stub]
            str_group_R = f'.FUNC' + ' ' + ' '.join("{:<20}".format(g) for g in group)
            R = R_eq[:, i]
            for j in range(len(frequency)):
                str_group_R = str_group_R + f'({frequency[j]},{R[j]})     '
            str_group_R = str_group_R + '}\n'
            str_R.append(str_group_R)

    #### Creating string for equivalent mutual inductance
    str_M = []
    if M_eq.size:
        for i in range(M_eq.shape[1]):
            group = [f'{element}_M_{i + 1}(1)', tab_stub]
            str_group_M = f'.FUNC' + ' ' + ' '.join("{:<20}".format(g) for g in group)
            M = M_eq[:, i]
            for j in range(len(frequency)):
                str_group_M = str_group_M + f'({frequency[j]},{np.real(M[j])}+{np.imag(M[j])}J)     '
            str_group_M = str_group_M + '}\n'
            str_M.append(str_group_M)

    ## Opening library file
    lib_path = path_file
    with open(lib_path) as f:
        lines = f.readlines()

    ## Changing elements in library
    for k in range(len(lines)):
        line = lines[k]
        for i in range(M_eq.shape[1]*2):
            if line.startswith(f'.FUNC {element}_L_{i+1}(1)') and str_L:
                lines[k] = str_L[i]
            elif line.startswith(f'.FUNC {element}_R_{i+1}(1)') and str_R:
                lines[k] = str_R[i]
            elif line.startswith(f'.FUNC {element}_M_{i+1}(1)') and str_M:
                lines[k] = str_M[i]

    text_lib = ''.join(lines)

    if not force_new_name:
        new_lib_path = Path('..//lib//MB_TFM_General_Adjusted.lib').resolve()
    else:
        new_lib_path = force_new_name
    with open(new_lib_path, 'w') as f:
        f.write(text_lib)
    return new_lib_path


def change_library_MutualCoupling(path_file: Path, element: str, frequency: np.ndarray, M_eq: np.ndarray):
    '''
    Helper function that changes the mutual coupling values of element to M_eq. Can be multiple values, e.g. a
    changing coupling over frequency
    '''

    #### Creating string for equivalent mutual inductance
    str_group_M = f'.FUNC {element}(1)					' + '{TABLE{FREQ} =  '
    for j in range(len(frequency)):
        str_group_M = str_group_M + f'({frequency[j]},{np.real(M_eq[j])}+{np.imag(M_eq[j])}J)     '
    str_group_M = str_group_M + '}\n'

    ## Opening library file
    lib_path = path_file
    with open(lib_path) as f:
         lines = f.readlines()

    ## Changing elements in library
    for k in range(len(lines)):
        line = lines[k]
        if line.startswith(f'.FUNC {element}(1)'):
            lines[k] = str_group_M

    text_lib = ''.join(lines)

    with open(path_file, 'w') as f:
        f.write(text_lib)
    return path_file

########################################################################################################################
################################################### HELPER FUNCTIONS   #################################################
def smooth_curve(y: np.ndarray, box_pts: int, n_pad: int = 20) -> np.ndarray:
    '''
    Helper function that smoothes a curve with a box filter
    :param y: np.ndarray - Array to be smoothed
    :param box_pts: int - width of the box filter (generally 3 or 5)
    :param n_pad: int - width of zero-padding
    :return: the smoothed array
    '''
    box = np.ones(box_pts) / box_pts
    if len(y.shape)>1:
        y_smooth = np.zeros(y.shape)
        for i in range(y.shape[0]):
            y_padded = np.pad(y[i,:], n_pad, mode='constant',constant_values=(y[i,0],y[i,-1]))
            y_filtered = np.convolve(y_padded, box, mode='same')
            y_smooth[i, :] = y_filtered[n_pad:-n_pad]
    else:
        y_padded = np.pad(y, n_pad, mode='constant', constant_values=(y[0], y[-1]))
        y_smooth = np.convolve(y_padded, box, mode='same')
    return y_smooth[n_pad: -n_pad]


def is_positive_definite(matrix):
    return np.all(np.linalg.eigvals(matrix) >= 0)


def check_smoothness(frequency: np.ndarray, signal: np.ndarray):
    '''

    '''
    derivative = np.diff(signal) / np.diff(frequency)
    zero_crossings = np.where(np.diff(np.sign(signal)))[0]
    for idx in zero_crossings:
        if idx > 0 and idx < len(derivative) - 1:
            derivative_diff = abs(derivative[idx + 1] - derivative[idx])
            if derivative_diff > np.median(abs(derivative)):
                signal[idx + 1:] *= -1
                derivative = np.diff(signal) / np.diff(frequency)
    smooth_signal = smooth_curve(signal, 5, n_pad=5)
    return smooth_signal


def interpolate_curve(signal: np.ndarray):
    '''

    :param signal:
    :type signal:
    :return:
    :rtype:
    '''
    def detect_spikes_in_derivative(signal, distance=5, prominence=1):
        derivative = np.diff(signal)
        peaks, _ = find_peaks(np.abs(derivative), distance=distance, prominence=0.2*np.abs(derivative).max())
        return peaks, derivative

    def smooth_signal_around_spikes(signal, spike_indices, window_size):
        smooth_signal = np.copy(signal)
        for spike_index in spike_indices:
            start_index = max(0, spike_index - window_size)
            end_index = min(len(signal), spike_index + window_size)
            x = np.arange(0, start_index).tolist() + np.arange(end_index, len(signal)).tolist()
            y = smooth_signal[:start_index].tolist() + smooth_signal[end_index:].tolist()
            f_interp = interp1d(x, y, kind='linear', fill_value="extrapolate")
            smooth_signal[start_index:end_index] = f_interp(np.arange(start_index, end_index))
        return smooth_signal

    spike_indices, derivative = detect_spikes_in_derivative(signal, distance=1, prominence=1.5)
    window_size = 10  # Number of points around the spike to interpolate
    smooth_signal = smooth_signal_around_spikes(signal, spike_indices, window_size)
    return smooth_signal

import numpy as np
from dataclasses import dataclass, field
from pydantic import BaseModel, create_model, Field
from typing import Any, Dict, List, Optional, Union

"""
    This class defines the TFM dataclasses, which contain the variables to be used in the TFM model.
"""


'''New code'''

@dataclass
class General:
    magnet_name: Optional[str] = None
    magnet_length: Optional[float] = None
    num_HalfTurns: Optional[int] = None
    I_magnet: Optional[float] = None
    groups: Optional[int] = None
    local_library_path: Optional[str] = None
    lib_path: Optional[str] = None
    new_lib_path: Optional[str] = None
    L_mag: Optional[float] = None
    C_ground: Optional[float] = None
    R_warm: Optional[float] = None
    apertures: Optional[int] = None
    COMSOL_ap: Optional[int] = None
    sections_to_apertures: np.ndarray = field(default_factory=lambda: np.array([]))
    inductance_to_section: np.ndarray = field(default_factory=lambda: np.array([]))
    el_order_sections: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class Shorts:
    sections_to_short: Optional[list] = None
    short_resistances: Optional[list] = None


@dataclass
class Turns:
    turns_to_sections: np.ndarray = field(default_factory=lambda: np.array([]))
    turns_to_apertures: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class HalfTurns:
    HalfTurns_to_apertures: np.ndarray = field(default_factory=lambda: np.array([]))
    HalfTurns_to_groups: np.ndarray = field(default_factory=lambda: np.array([]))
    HalfTurns_to_conductor: np.ndarray = field(default_factory=lambda: np.array([]))
    HalfTurns_to_sections: np.ndarray = field(default_factory=lambda: np.array([]))
    n_strands: np.ndarray = field(default_factory=lambda: np.array([]))
    rotation_ht: np.ndarray = field(default_factory=lambda: np.array([]))
    mirror_ht: np.ndarray = field(default_factory=lambda: np.array([]))
    alphaDEG_ht: np.ndarray = field(default_factory=lambda: np.array([]))
    bare_cable_width: np.ndarray = field(default_factory=lambda: np.array([]))
    bare_cable_height_mean: np.ndarray = field(default_factory=lambda: np.array([]))
    strand_twist_pitch: np.ndarray = field(default_factory=lambda: np.array([]))
    Nc: np.ndarray = field(default_factory=lambda: np.array([]))
    C_strand: np.ndarray = field(default_factory=lambda: np.array([]))
    Rc: np.ndarray = field(default_factory=lambda: np.array([]))
    RRR: np.ndarray = field(default_factory=lambda: np.array([]))
    diameter: np.ndarray = field(default_factory=lambda: np.array([]))
    fsc: np.ndarray = field(default_factory=lambda: np.array([]))
    f_rho_effective: np.ndarray = field(default_factory=lambda: np.array([]))
    R_warm: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class Strands:
    filament_diameter: np.ndarray = field(default_factory=lambda: np.array([]))
    diameter: np.ndarray = field(default_factory=lambda: np.array([]))
    d_filamentary: np.ndarray = field(default_factory=lambda: np.array([]))
    d_core: np.ndarray = field(default_factory=lambda: np.array([]))
    fsc: np.ndarray = field(default_factory=lambda: np.array([]))
    f_rho_effective: np.ndarray = field(default_factory=lambda: np.array([]))
    fil_twist_pitch: np.ndarray = field(default_factory=lambda: np.array([]))
    RRR: np.ndarray = field(default_factory=lambda: np.array([]))
    f_mag_X_Roxie: np.ndarray = field(default_factory=lambda: np.array([]))
    f_mag_Y_Roxie: np.ndarray = field(default_factory=lambda: np.array([]))
    f_mag_Roxie: np.ndarray = field(default_factory=lambda: np.array([]))
    f_mag_Comsol: np.ndarray = field(default_factory=lambda: np.array([]))
    f_mag_X_Comsol: np.ndarray = field(default_factory=lambda: np.array([]))
    f_mag_Y_Comsol: np.ndarray = field(default_factory=lambda: np.array([]))
    strands_to_conductor: np.ndarray = field(default_factory=lambda: np.array([]))
    strands_to_sections: np.ndarray = field(default_factory=lambda: np.array([]))
    strands_to_apertures: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class Options:
    flag_SC: Optional[bool] = True
    flag_Wedge: Optional[bool] = False
    flag_CPS: Optional[bool] = False
    flag_AlRing: Optional[bool] = False
    flag_BS: Optional[bool] = False
    flag_CB: Optional[bool] = False
    flag_ED: Optional[bool] = False
    flag_ISCC: Optional[bool] = False
    flag_IFCC: Optional[bool] = False
    flag_PC: Optional[bool] = False


@dataclass
class PC:  # DataClass for persistent current
    L: np.ndarray = field(default_factory=lambda: np.array([]))  # Inductance for PC modelisation
    I: np.ndarray = field(default_factory=lambda: np.array([]))  # Current generator for PC modelisation
    M: np.ndarray = field(default_factory=lambda: np.array([]))  # Coupling factor for PC modelisation
    M_PC_IFCC: np.ndarray = field(default_factory=lambda: np.array([]))  # Coupling factor between PC currents and interfilament currents
    M_strands: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class IFCC:
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))
    R_strands: np.ndarray = field(default_factory=lambda: np.array([]))
    M_strands: np.ndarray = field(default_factory=lambda: np.array([]))
    I_strands: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class ISCC:
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))
    R_halfturns: np.ndarray = field(default_factory=lambda: np.array([]))
    M_halfturns: np.ndarray = field(default_factory=lambda: np.array([]))
    I_halfturns: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class ED:
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))
    R_strands: np.ndarray = field(default_factory=lambda: np.array([]))
    M_strands: np.ndarray = field(default_factory=lambda: np.array([]))
    I_strands: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class Wedge:
    RRR_Wedge: float = field(default_factory=lambda: None)
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class CB:
    r_CB: float = field(default_factory=lambda: None)
    t_CB: float = field(default_factory=lambda: None)
    f_SS: float = field(default_factory=lambda: None)
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class BS:
    T_BS: float = field(default_factory=lambda: None)
    f_SS: float = field(default_factory=lambda: None)
    r_BS: float = field(default_factory=lambda: None)
    RRR_ApA_1: float = field(default_factory=lambda: None)
    RRR_ApA_2: float = field(default_factory=lambda: None)
    RRR_ApB_1: float = field(default_factory=lambda: None)
    RRR_ApB_2: float = field(default_factory=lambda: None)
    t_ApA_1: float = field(default_factory=lambda: None)
    t_ApA_2: float = field(default_factory=lambda: None)
    t_SS_A: float = field(default_factory=lambda: None)
    t_ApB_1: float = field(default_factory=lambda: None)
    t_ApB_2: float = field(default_factory=lambda: None)
    t_SS_B: float = field(default_factory=lambda: None)
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class CPS:
    group_CPS: int = field(default_factory=lambda: None)
    rho_CPS: Union[str, float] = field(default_factory=lambda: None)
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))


@dataclass
class AlRing:
    rho_AlRing: float = field(default_factory=lambda: None)
    L: np.ndarray = field(default_factory=lambda: np.array([]))
    R: np.ndarray = field(default_factory=lambda: np.array([]))
    M: np.ndarray = field(default_factory=lambda: np.array([]))
    I: np.ndarray = field(default_factory=lambda: np.array([]))
    P: np.ndarray = field(default_factory=lambda: np.array([]))
    tau: np.ndarray = field(default_factory=lambda: np.array([]))


########################################################################################################################
################################### TRANSLATE FUNCTIONS OF LEDET DATA TO TFM DATA  #####################################

def lookupModelDataToTFMHalfTurns(key: str):
    """
     Retrieves the correct HalfTurnsTFM parameter name for a DataModelMagnet input
    """
    lookup = {
        'nStrands_inGroup': 'n_strands',
        'wBare_inGroup': 'bare_cable_width',
        'hBare_inGroup': 'bare_cable_height_mean',
        'Lp_s_inGroup': 'strand_twist_pitch',
        'R_c_inGroup': 'Rc',
        'RRR_Cu_inGroup': 'RRR',
        'ds_inGroup': 'diameter',
        'f_SC_strand_inGroup': 'fsc',
        'f_ro_eff_inGroup': 'f_rho_effective',

        'alphasDEG': 'alphaDEG_ht',
        'rotation_block': 'rotation_ht',
        'mirror_block': 'mirror_ht'
    }

    returned_key = lookup[key] if key in lookup else None
    return returned_key


def lookupModelDataToTFMStrands(key: str):
    """
    Retrieves the correct StrandsTFM parameter name for a DataModelMagnet input
    """
    lookup = {
        'df_inGroup': 'filament_diameter',
        'ds_inGroup': 'diameter',
        'f_SC_strand_inGroup': 'fsc',
        'f_ro_eff_inGroup': 'f_rho_effective',
        'Lp_f_inGroup': 'fil_twist_pitch',
        'RRR_Cu_inGroup': 'RRR',
        'dfilamentary_inGroup': 'd_filamentary',
        'dcore_inGroup': 'd_core',
    }

    returned_key = lookup[key] if key in lookup else None
    return returned_key


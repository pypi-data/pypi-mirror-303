from typing import Union

import numpy as np
import numpy.typing as npt

def geodetic2ECEF(
    rrmLLA: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_semi_major_axis: float,
    m_semi_minor_axis: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ECEF2geodetic(
    mmmXYZ: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_semi_major_axis: float,
    m_semi_minor_axis: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ECEF2ENU(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_target: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_semi_major_axis: float,
    m_semi_minor_axis: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ECEF2NED(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_target: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_semi_major_axis: float,
    m_semi_minor_axis: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ECEF2ENUv(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_target: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ECEF2NEDv(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_target: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ENU2ECEF(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_local: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_semi_major_axis: float,
    m_semi_minor_axis: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def NED2ECEF(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_local: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_semi_major_axis: float,
    m_semi_minor_axis: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ENU2ECEFv(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_local: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def NED2ECEFv(
    rrmLLA_local_origin: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    mmmXYZ_local: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def ENU2AER(
    mmmENU: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def AER2ENU(
    rrmAER: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def NED2AER(
    mmmNED: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def AER2NED(
    rrmAER: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...

from typing import Union

import numpy as np
import numpy.typing as npt

def Haversine(
    rrmStart: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    rrmEnd: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
    m_radius_sphere: float,
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...

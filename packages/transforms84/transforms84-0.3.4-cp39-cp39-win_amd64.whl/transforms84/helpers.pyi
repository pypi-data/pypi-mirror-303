from typing import Union

import numpy as np
import numpy.typing as npt

def deg_angular_difference(
    angle1: Union[
        float,
        npt.NDArray[
            Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
        ],
    ],
    angle2: Union[
        float,
        npt.NDArray[
            Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
        ],
    ],
    smallest_angle: bool,
) -> Union[
    float,
    npt.NDArray[Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]],
]: ...
def rad_angular_difference(
    angle1: Union[
        float,
        npt.NDArray[
            Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
        ],
    ],
    angle2: Union[
        float,
        npt.NDArray[
            Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
        ],
    ],
    smallest_angle: bool,
) -> Union[
    float,
    npt.NDArray[Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]],
]: ...
def RRM2DDM(
    rrm_position: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def DDM2RRM(
    ddm_position: npt.NDArray[
        Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
    ],
) -> npt.NDArray[
    Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]
]: ...
def wrap(
    num: Union[
        float,
        int,
        npt.NDArray[Union[np.float32, np.float64]],
    ],
    bound_lower: Union[
        float,
        int,
        npt.NDArray[Union[np.float32, np.float64]],
    ],
    bound_upper: Union[
        float,
        int,
        npt.NDArray[Union[np.float32, np.float64]],
    ],
) -> Union[
    float,
    npt.NDArray[Union[np.float32, np.float64, np.int8, np.int16, np.int32, np.int64]],
]: ...

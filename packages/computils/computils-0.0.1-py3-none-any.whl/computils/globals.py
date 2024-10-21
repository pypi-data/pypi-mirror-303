""" This module collects all exposed types."""

import numpy as np
from enum import Enum
from abc import ABC, abstractmethod
from typing import final, Union

MACHINE_EPS: final = float(2 ** (-53))  # max relative error corresponding to 1/2 ULP
SQUARE_ROOT_MACHINE_EPS: final = np.sqrt(MACHINE_EPS)
CUBE_ROOT_MACHINE_EPS: final = np.cbrt(MACHINE_EPS)
FOURTH_ROOT_MACHINE_EPS: final = np.power(MACHINE_EPS, 1/4)

Integer: final = Union[int, np.int8, np.int16, np.int32, np.int64, np.uint8, np.uint16, np.uint32, np.uint64]
Float: final = Union[float, np.float16, np.float32, np.float64, np.float128]
Complex: final = Union[complex, np.complex64, np.complex128, np.complex256]
Scalar: final = Union[Integer, Float, Complex]

IntOrArray: final = Union[Integer, np.ndarray]
FloatOrArray: final = Union[Float, np.ndarray]
ComplexOrArray: final = Union[Complex, np.ndarray]
ScalarOrArray: final = Union[Scalar, np.ndarray]


# 128-bit integers generated using entropy gathered from the OS, for fixing the seed of NumPy generators.
SEED128_1: final = 137088887599416403785824428186011523708
SEED128_2: final = 230453062773196406322953725600125856954
SEED128_3: final = 334883455271001690768699206953238296696
SEED128_4: final = 69805789651723487751993596682833892465
SEED128_5: final = 107997836754270478432192384195731366045
SEED128_6: final = 61384398454038591198002507585631369346
SEED128_7: final = 165303562401480433055547884045914282112
SEED128_8: final = 215418768511176275020128984871223831370
SEED128_9: final = 247520618467519227348322182729719821192
SEED128_10: final = 260473913589332506348144405693894964574


class InterpolationType(Enum):
    linear = 0
    ncs = 1  # natural cubic spline
    ccs = 2  # clamped cubic spline
    pmc = 3  # piecewise monotone cubic [FC80]
    pchip = 4  # [FB84]


class ExtrapolationType(Enum):
    nan = 0
    flat = 1


class Interpolator(ABC):
    def __init__(self,
                 inter_type: InterpolationType,
                 extra_type: ExtrapolationType):

        self.inter_type: InterpolationType = inter_type
        self.extra_type: ExtrapolationType = extra_type

    @abstractmethod
    def __call__(self, x: ScalarOrArray) -> ScalarOrArray:
        """

        :param x:
        :return:
        """

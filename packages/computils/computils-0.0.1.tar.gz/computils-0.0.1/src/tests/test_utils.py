"This module collects functionality for testing. "

import numpy as np
from computils import FloatOrArray


def compute_max_abs_diff(expected: np.ndarray, actual: np.ndarray) -> float:
    return float(np.amax(compute_abs_diff(expected, actual)))


def compute_abs_diff(expected: FloatOrArray, actual: FloatOrArray) -> FloatOrArray:
    return np.abs(actual - expected)
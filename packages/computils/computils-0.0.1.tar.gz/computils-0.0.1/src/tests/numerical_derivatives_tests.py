""" This module tests the computation of numerical derivatives. """

import unittest
import numpy as np
from computils.finite_difference import compute_gradient, compute_jacobian, compute_hessian


def func_r2_to_r3(x: np.ndarray, scaling_factor: float = 1.0) -> np.ndarray:
    """ A test function f: R^2 -> R^3

    :param x: a (2,) np array of argument values.
    :param scaling_factor: real number (nonzero).
    :return: a (3,) array containing the function values
    """

    function_values = np.zeros((3,))
    function_values[0] = 2.0 * x[0]
    function_values[1] = func_r2_to_r(x)
    function_values[2] = -3.0 * x[1]
    
    return scaling_factor * function_values


def analytical_jacobian_test_func_r2_to_r3(x: np.ndarray) -> np.ndarray:
    """ Analytical Jacobian of the test function f: R^2 -> R^3

    :param x: a (2,) np array of argument values.
    :return: jacobian: a (3, 2) array of first-order derivatives.
    """
    
    jacobian = np.zeros((3, 2))
    jacobian[0, 0] = 2.0
    jacobian[1, :] = analytical_gradient_test_func_r2_to_r(x).flatten()
    jacobian[2, 1] = -3.0
    return jacobian


def func_r2_to_r(x: np.ndarray, scaling_factor: float = 1.0) -> float:
    """ A test function f: R^2 -> R

    :param x: a (2,) array of argument values.
    :param scaling_factor: real number (nonzero).
    :return: the function value (scalar).
    """

    return scaling_factor * (2.0 * x[0] ** 2 + 4.0 * x[1] ** 3 + 6.0 * x[0] * x[1])


def analytical_gradient_test_func_r2_to_r(x: np.ndarray) -> np.ndarray:
    """ Analytical gradient of the test function f: R^2 -> R

    :param x: a (2,) array of argument values.
    :return: gradient: a (2, 1) np array of first-order derivatives.
    """

    gradient = np.zeros((2, 1))
    gradient[0, 0] = 4.0 * x[0] + 6.0 * x[1]
    gradient[1, 0] = 12.0 * x[1] ** 2 + 6.0 * x[0]
    return gradient


def analytical_hessian_test_func_r2_to_r(x: np.ndarray) -> np.ndarray:
    """ Analytical hessian of the test function f: R^2 -> R

    :param x: a (2,) array of argument values.
    :return: hessian: a (2, 1) np array of first-order derivatives.
    """

    hessian = np.zeros((2, 2))
    hessian[0, 0] = 4.0
    hessian[0, 1] = hessian[1, 0] = 6.0
    hessian[1, 1] = 24.0 * x[1]
    return hessian


class FiniteDifferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.x_values = [n * np.array([0.5, 1.0]) for n in range(-1, 10)]
        cls.scaling_factor = 0.9

    def test_gradient(self):
        for x in self.x_values:
            for include_args in (True, False):
                analytical_gradient = analytical_gradient_test_func_r2_to_r(x)

                if include_args:
                    analytical_gradient *= self.scaling_factor
                    numerical_gradient = compute_gradient(func_r2_to_r, x, args=(self.scaling_factor,))
                else:
                    numerical_gradient = compute_gradient(func_r2_to_r, x)

                diffs = numerical_gradient - analytical_gradient
                max_diff = np.amax(np.abs(diffs))
                self.assertAlmostEqual(0.0, max_diff, delta=10**-8)

    def test_jacobian(self):
        for x in self.x_values:
            for include_args in (True, False):
                analytical_jacobian = analytical_jacobian_test_func_r2_to_r3(x)

                if include_args:
                    analytical_jacobian *= self.scaling_factor
                    numerical_jacobian = compute_jacobian(func_r2_to_r3, x, args=(self.scaling_factor,))
                else:
                    numerical_jacobian = compute_jacobian(func_r2_to_r3, x)

                diffs = numerical_jacobian - analytical_jacobian
                max_diff = np.amax(np.abs(diffs))
                self.assertAlmostEqual(0.0, max_diff, delta=10**-8)

    def test_hessian(self):
        for x in self.x_values:
            for include_args in (True, False):
                analytical_hessian = analytical_hessian_test_func_r2_to_r(x)

                if include_args:
                    analytical_hessian *= self.scaling_factor
                    numerical_hessian = compute_hessian(func_r2_to_r, x, args=(self.scaling_factor,))
                else:
                    numerical_hessian = compute_hessian(func_r2_to_r, x)

                diffs = numerical_hessian - analytical_hessian
                max_diff = np.amax(np.abs(diffs))
                self.assertAlmostEqual(0.0, max_diff, delta=10**-6)


if __name__ == '__main__':
    unittest.main()

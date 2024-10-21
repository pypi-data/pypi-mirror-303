""" This module contains transformations and their inverse functions for imposing parameter restrictions. """

import numpy as np


def impose_lower_bound(transformed_parameter: float, lower_bound: float) -> float:
    return np.exp(transformed_parameter) + lower_bound


def inverse_impose_lower_bound(parameter: float, lower_bound: float) -> float:
    return np.log(parameter - lower_bound)


def impose_upper_bound(transformed_parameter: float, upper_bound: float) -> float:
    return -np.exp(transformed_parameter) + upper_bound


def inverse_impose_upper_bound(parameter: float, upper_bound: float) -> float:
    return np.log(upper_bound - parameter)


def impose_bounds(transformed_parameter: float, lower_bound: float, upper_bound: float) -> float:
    return lower_bound + (upper_bound - lower_bound)/(1.0 + np.exp(-transformed_parameter))


def inverse_impose_bounds(parameter: float, lower_bound: float, upper_bound: float) -> float:
    z = (parameter - lower_bound)/(upper_bound - lower_bound)
    return np.log(z) - np.log(1.0 - z)


def impose_upper_bound_sum(transformed_params: np.ndarray, upper_bound: float) -> np.ndarray:
    """ Imposes an upper bound on the sum of params, such that all params are in (0, upper_bound).

    :param transformed_params: (n_params,) array of transformed parameters, real numbers
    :param upper_bound: real number
    :return: constrained_params: (n_params,) array of parameters with constraints
    """

    exp_trans_params = np.exp(transformed_params)
    constrained_params = upper_bound * np.divide(exp_trans_params, np.sum(exp_trans_params) + 1.0)
    return constrained_params


def inverse_impose_upper_bound_sum(params: np.ndarray, upper_bound: float) -> np.ndarray:
    """  Inverse transformation function of impose_upper_bound_sum.

    :param params: (n_params,) array of params that are all in (0, upper_bound)
    :param upper_bound: real number
    :return: unconstrained_params
    """

    sum_params = np.sum(params)
    unconstrained_params = np.log(params / (upper_bound - sum_params))
    return unconstrained_params

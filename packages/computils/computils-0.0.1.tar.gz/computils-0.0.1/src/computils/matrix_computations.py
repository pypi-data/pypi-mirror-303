""" This module contains functionality related to matrix computations. """

import numpy as np
from numpy.linalg import solve


def robust_inverse(square_matrix: np.ndarray) -> np.ndarray:
    """ Computes the inverse of the square matrix.

    :param square_matrix: (n, n) array corresponding to an invertible matrix.
    :return: inverse_matrix: (n, n) array.
    """

    if is_diagonal(square_matrix):
        main_diagonal_inverse = np.divide(1.0, np.diagonal(square_matrix))
        return np.diag(main_diagonal_inverse)
    else:
        inverse_matrix = solve(square_matrix, np.eye(square_matrix.shape[0]))
        return inverse_matrix


def is_diagonal(matrix: np.ndarray) -> bool:
    return np.count_nonzero(matrix - np.diag(np.diagonal(matrix))) == 0

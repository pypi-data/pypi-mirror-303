""" This module implements functionality related to Gaussian elimination with scaled partial pivoting. """

import numpy as np
from numba import jit


def compute_inverse_using_gauss_elim_spp(square_matrix: np.ndarray) -> np.ndarray:
    """ Uses Gaussian elimination with scaled partial pivoting to compute the inverse of the given square matrix. """

    n_rows = square_matrix.shape[0]
    b = np.eye(n_rows)
    echelon_matrix = perform_gauss_elim_spp(a=square_matrix, b=b)
    reduced_matrix = perform_back_substitution(echelon_matrix)
    inverse_matrix = reduced_matrix[:, n_rows:]
    return inverse_matrix


def perform_gauss_elim_spp(a: np.ndarray,
                           b: np.ndarray) -> np.ndarray:
    """ Performs Gaussian elimination with scaled partial pivoting to put the matrix [a b] in echelon form.

    :param a: an (n, n) array representing a square matrix.
    :param b: an (n, n_b) array.
    :return: echelon_matrix: an (n, n + n_b) matrix corresponding to [a b] in reduced echelon form, in which
        the rows may have been swapped.
    """

    echelon_matrix = np.hstack((a, b))
    n_rows = a.shape[0]

    for j in range(n_rows - 1):
        submatrix_a_right_to_pivot = echelon_matrix[j:, (j + 1):n_rows]
        max_value_per_row = np.amax(np.abs(submatrix_a_right_to_pivot), axis=1)
        r = np.divide(np.abs(echelon_matrix[j:, j]), max_value_per_row)
        k = j + np.argmax(r)  # k = row with largest r_k

        if j != k:
            echelon_matrix[[j, k]] = echelon_matrix[[k, j]]  # swap rows

        for i in range(j + 1, n_rows):
            ratio = echelon_matrix[i, j] / echelon_matrix[j, j]
            echelon_matrix[i, :] -= ratio * echelon_matrix[j, :]

    return echelon_matrix


def perform_back_substitution(echelon_matrix: np.ndarray) -> np.ndarray:
    """ Transforms a matrix in echelon form to reduced echelon form using back substitution.
    
    :param echelon_matrix: a matrix [A B] in echelon form.
    :return: reduced_matrix: the result of the matrix [A B] after back substitution.
    """

    reduced_matrix = echelon_matrix.copy()
    n_rows = reduced_matrix.shape[0] 
    for j in reversed(range(n_rows)):
        reduced_matrix[j, j:] /= reduced_matrix[j, j]
    
        for i in range(j):
            reduced_matrix[i, j:] -= reduced_matrix[i, j] * reduced_matrix[j, j:]
        
    return reduced_matrix

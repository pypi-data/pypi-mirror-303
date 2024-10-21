""" This module tests functionality related to matrix computations. """

import unittest
import numpy as np
from numpy.linalg import inv
from scipy.stats import wishart
from test_utils import compute_max_abs_diff
from computils import SEED128_1
from computils.gaussian_elim_spp import compute_inverse_using_gauss_elim_spp


class MatrixComputationsTests(unittest.TestCase):

    def test_inverse_gauss_elim_spp(self):
        rng = np.random.default_rng(SEED128_1)
        n = 50
        df = n + 1.0
        scale_matrix = np.eye(n)

        for i in range(100):
            matrix = wishart.rvs(df=df, scale=scale_matrix, random_state=rng)
            inverse_matrix = inv(matrix)
            inverse_matrix_gespp = compute_inverse_using_gauss_elim_spp(matrix)
            max_diff = compute_max_abs_diff(inverse_matrix, inverse_matrix_gespp)
            self.assertAlmostEqual(0.0, max_diff, delta=10**-8)

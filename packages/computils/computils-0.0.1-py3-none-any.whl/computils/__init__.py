""" This module serves as the interface of the computils package.

    References:
        FC80: Frederick N. Fritsch and Ralph E. Carlson. Monotone piecewise cubic interpolation. SIAM Journal on
            Numerical Analysis, 17(2):238–246, 1980. doi:10.1137/0717021.
        FB84: Frederick N. Fritsch and Judy Butland. A method for constructing local monotone piecewise cubic
            interpolants. SIAM Journal on Scientific and Statistical Computing, 5(2):300–304, 1984. doi:10.1137/0905021.
"""

from .globals import *
from .factory import create_interpolator
from .sorting_algorithms import index_eq, find_le, find_ge, find_gt, find_lt
from .finite_difference import compute_derivative, compute_gradient, compute_jacobian, compute_hessian
from .type_utils import size
from .fast_eval import fast_matrix_inversion, fast_determinant, fast_quadratic_form, fast_diag_mult_AD, \
    fast_diag_mult_DA, fast_columnwise_bilinear_form
from .gaussian_elim_spp import compute_inverse_using_gauss_elim_spp
from .matrix_computations import robust_inverse, is_diagonal
from .parameter_transformations import impose_lower_bound, inverse_impose_lower_bound, impose_upper_bound, \
    inverse_impose_upper_bound, impose_bounds, inverse_impose_bounds, impose_upper_bound_sum, \
    inverse_impose_upper_bound_sum
from .performance_checking import compute_average_running_time

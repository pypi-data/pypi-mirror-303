""" This module implements tests for the parameter transformation functions. """

import unittest
import numpy as np
import computils.parameter_transformations as pt


class ParameterTransformationTests(unittest.TestCase):
    def test_impose_lower_bound(self):
        n_values = 100
        lower_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for lower_bound in lower_bounds:
            expected_value = 1.0 + lower_bound
            actual_value = pt.impose_lower_bound(transformed_parameter=0.0, lower_bound=lower_bound)

            self.assertAlmostEqual(expected_value, actual_value, delta=10 ** (-10))

    def test_consistency_lower_bound_transformations(self):
        """ Tests consistency of the lower bound transformations by checking whether their
            composition yields the identity function. """

        n_values = 100
        lower_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)
        transformed_values = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for lower_bound in lower_bounds:
            for value in transformed_values:
                actual_value = pt.inverse_impose_lower_bound(
                    pt.impose_lower_bound(value, lower_bound), lower_bound)

                self.assertAlmostEqual(value, actual_value, delta=10 ** (-10))

    def test_impose_upper_bound(self):
        n_values = 100
        upper_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for upper_bound in upper_bounds:
            expected_value = -1.0 + upper_bound
            actual_value = pt.impose_upper_bound(transformed_parameter=0.0, upper_bound=upper_bound)

            self.assertAlmostEqual(expected_value, actual_value, delta=10 ** (-10))

    def test_consistency_upper_bound_transformations(self):
        """ Tests consistency of the upper bound transformations by checking whether their
            composition yields the identity function. """

        n_values = 100
        upper_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)
        transformed_values = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for upper_bound in upper_bounds:
            for value in transformed_values:
                actual_value = pt.inverse_impose_upper_bound(
                    pt.impose_upper_bound(value, upper_bound), upper_bound)

                self.assertAlmostEqual(value, actual_value, delta=10 ** (-10))

    def test_impose_bounds(self):
        n_values = 100
        lower_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)
        upper_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for lower_bound in lower_bounds:
            for upper_bound in upper_bounds:
                expected_value = (lower_bound + upper_bound) / 2.0
                actual_value = pt.impose_bounds(
                    transformed_parameter=0.0, lower_bound=lower_bound, upper_bound=upper_bound)

                self.assertAlmostEqual(expected_value, actual_value, delta=10 ** (-10))

    def test_consistency_bounds_transformations(self):
        """ Tests consistency of the double bound transformations by checking whether their
            composition yields the identity function. """

        n_values = 100
        lower_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)
        transformed_values = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for lower_bound in lower_bounds:
            upper_bound = lower_bound + 1.0

            for value in transformed_values:
                actual_value = pt.inverse_impose_bounds(
                    pt.impose_bounds(value, lower_bound, upper_bound), lower_bound, upper_bound)

                self.assertAlmostEqual(value, actual_value, delta=10 ** (-10))

    def test_impose_upper_bound_sum(self):
        n_params = 3
        transformed_params = np.zeros((n_params,))
        n_values = 100
        upper_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)

        for upper_bound in upper_bounds:
            expected_param_value = upper_bound / (n_params + 1.0)
            actual_params = pt.impose_upper_bound_sum(transformed_params=transformed_params, upper_bound=upper_bound)

            for param in actual_params:
                self.assertAlmostEqual(expected_param_value, param, delta=10 ** (-10))

    def test_consistency_upper_bound_sum_transformations(self):
        """ Tests consistency of the upper bound sum transformations by checking whether their
            composition yields the identity function. """

        n_values = 100
        upper_bounds = np.linspace(start=-10.0, stop=10.0, num=n_values)
        transformed_values = np.random.normal(size=(n_values, 2))

        for upper_bound in upper_bounds:
            for i in range(n_values):
                transformed_params = transformed_values[i]
                result = pt.inverse_impose_upper_bound_sum(
                    pt.impose_upper_bound_sum(transformed_params, upper_bound), upper_bound)

                diffs = result - transformed_params
                max_abs_diff = np.amax(np.abs(diffs))
                self.assertAlmostEqual(0.0, max_abs_diff, delta=10 ** (-10))


if __name__ == '__main__':
    unittest.main()

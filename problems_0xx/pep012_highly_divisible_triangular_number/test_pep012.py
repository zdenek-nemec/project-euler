import unittest

from parameterized import parameterized

from problems_0xx.pep012_highly_divisible_triangular_number.pep012 import ProjectEulerProblem012


class ProjectEulerProblem012Test(unittest.TestCase):
    @parameterized.expand([
        [5, 28],
        [500, 76576500]])
    def test_solve(self, divisors_limit, expected_triangle_number):
        actual_triangle_number = ProjectEulerProblem012(divisors_limit).solve()
        self.assertEqual(
            expected_triangle_number,
            actual_triangle_number,
            "Failed for limit of %d divisors."
            % divisors_limit)


if __name__ == "__main__":
    pass

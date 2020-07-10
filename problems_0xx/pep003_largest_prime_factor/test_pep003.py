import unittest

from parameterized import parameterized

from problems_0xx.pep003_largest_prime_factor.pep003 import ProjectEulerProblem003


class ProjectEulerProblem003Test(unittest.TestCase):
    @parameterized.expand([
        [13195, 29],
        [600851475143, 6857]])
    def test_solve(self, number, expected_prime_factor):
        actual_prime_factor = ProjectEulerProblem003(number).solve()
        self.assertEqual(
            expected_prime_factor,
            actual_prime_factor,
            "Failed for the number %d."
            % number)


if __name__ == "__main__":
    pass

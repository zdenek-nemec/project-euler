import unittest

from parameterized import parameterized

from problems_0xx.pep020_factorial_digit_sum.pep020 import ProjectEulerProblem020


class ProjectEulerProblem020Test(unittest.TestCase):
    @parameterized.expand([
        [10, 27],
        [100, 648]])
    def test_solve(self, number, expected_sum):
        actual_sum = ProjectEulerProblem020(number).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Failed for the number %d."
            % number)


if __name__ == "__main__":
    unittest.main()

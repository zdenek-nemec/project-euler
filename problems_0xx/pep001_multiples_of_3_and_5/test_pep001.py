import unittest

from parameterized import parameterized

from problems_0xx.pep001_multiples_of_3_and_5.pep001 import ProjectEulerProblem001


class ProjectEulerProblem001Test(unittest.TestCase):
    @parameterized.expand([
        [[3, 5], 10, 23],
        [[3, 5], 1000, 233168]])
    def test_solve(self, multipliers, limit, expected_sum):
        actual_sum = ProjectEulerProblem001(multipliers, limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Actual and expected sums do not match.")


if __name__ == "__main__":
    unittest.main()

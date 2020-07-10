import unittest

from parameterized import parameterized

from problems_0xx.pep002_even_fibonacci_numbers.pep002 import ProjectEulerProblem002


class ProjectEulerProblem002Test(unittest.TestCase):
    @parameterized.expand([
        [[1, 2], 4000000, 4613732]])
    def test_solve(self, start, limit, expected_sum):
        actual_sum = ProjectEulerProblem002(start, limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Actual and expected sums do not match.")


if __name__ == "__main__":
    pass

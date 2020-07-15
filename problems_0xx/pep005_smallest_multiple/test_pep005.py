import unittest

from parameterized import parameterized

from problems_0xx.pep005_smallest_multiple.pep005 import ProjectEulerProblem005


class ProjectEulerProblem005Test(unittest.TestCase):
    @parameterized.expand([
        [10, 2520],
        [20, 232792560]])
    def test_solve(self, divisor_limit, expected_number):
        actual_number = ProjectEulerProblem005(divisor_limit).solve()
        self.assertEqual(
            expected_number,
            actual_number,
            "Failed for divisor limit %d."
            % divisor_limit)


if __name__ == "__main__":
    unittest.main()

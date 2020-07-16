import unittest

from parameterized import parameterized

from problems_0xx.pep006_sum_square_difference.pep006 import ProjectEulerProblem006


class ProjectEulerProblem006Test(unittest.TestCase):
    @parameterized.expand([
        [10, 2640],
        [100, 25164150]])
    def test_solve(self, number_limit, expected_difference):
        actual_difference = ProjectEulerProblem006(number_limit).solve()
        self.assertEqual(
            expected_difference,
            actual_difference,
            "Failed for number limit %d."
            % number_limit)


if __name__ == "__main__":
    unittest.main()

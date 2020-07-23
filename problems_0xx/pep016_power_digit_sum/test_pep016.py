import unittest

from parameterized import parameterized

from problems_0xx.pep016_power_digit_sum.pep016 import ProjectEulerProblem016


class ProjectEulerProblem016Test(unittest.TestCase):
    @parameterized.expand([
        [15, 26],
        [1000, 1366]])
    def test_solve(self, power, expected_sum):
        actual_sum = ProjectEulerProblem016(power).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Failed for power of %d."
            % power)


if __name__ == "__main__":
    unittest.main()

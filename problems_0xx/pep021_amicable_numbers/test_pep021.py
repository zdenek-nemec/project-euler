import unittest

from parameterized import parameterized

from problems_0xx.pep021_amicable_numbers.pep021 import ProjectEulerProblem021


class ProjectEulerProblem021Test(unittest.TestCase):
    @parameterized.expand([
        [10000, 31626]])
    def test_solve(self, limit, expected_sum):
        actual_sum = ProjectEulerProblem021(limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Failed for limit %d."
            % limit)


if __name__ == "__main__":
    unittest.main()

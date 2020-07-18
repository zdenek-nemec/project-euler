import unittest

from parameterized import parameterized

from problems_0xx.pep010_summation_of_primes.pep010 import ProjectEulerProblem010


class ProjectEulerProblem010Test(unittest.TestCase):
    @parameterized.expand([
        [10, 17],
        [2000000, 142913828922]])
    def test_solve(self, limit, expected_sum):
        actual_sum = ProjectEulerProblem010(limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Failed for the limit %d."
            % limit)


if __name__ == "__main__":
    unittest.main()

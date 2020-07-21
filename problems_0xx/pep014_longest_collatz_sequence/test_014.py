import unittest

from parameterized import parameterized

from problems_0xx.pep014_longest_collatz_sequence.pep014 import ProjectEulerProblem014


class ProjectEulerProblem014Test(unittest.TestCase):
    @parameterized.expand([
        [1000000, 837799]])
    def test_solve(self, limit, expected_number):
        returned_number = ProjectEulerProblem014(limit).solve()
        self.assertEqual(
            expected_number,
            returned_number,
            "Failed for limit %d."
            % limit)


if __name__ == "__main__":
    unittest.main()

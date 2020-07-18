import unittest

from parameterized import parameterized

from problems_0xx.pep007_10001st_prime.pep007 import ProjectEulerProblem007


class ProjectEulerProblem007Test(unittest.TestCase):
    @parameterized.expand([
        [6, 13],
        [10001, 104743]])
    def test_solve(self, position, expected_prime):
        actual_prime = ProjectEulerProblem007(position).solve()
        self.assertEqual(
            expected_prime,
            actual_prime,
            "Failed for position %d."
            % position)


if __name__ == "__main__":
    unittest.main()

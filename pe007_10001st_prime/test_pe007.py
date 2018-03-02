import unittest

from parameterized import parameterized
from pe007_10001st_prime.pe007 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [6, 13],
        [10001, 104743]
    ])
    def test_solve(self, position, expected_prime):
        prime = Solution().solve(position)
        self.assertEqual(
            prime,
            expected_prime,
            "The result should be %d but is %d."
            % (expected_prime, prime))


if __name__ == "__main__":
    pass

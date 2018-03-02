import unittest

from parameterized import parameterized
from pe003_largest_prime_factor.pe003 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [13195, 29],
        [600851475143, 6857]
    ])
    def test_solve(self, number, expected_prime_factor):
        largest_prime_factor = Solution().solve(number)
        self.assertEqual(
            largest_prime_factor,
            expected_prime_factor,
            'The result should be %d but is %d.'
            % (expected_prime_factor, largest_prime_factor))


if __name__ == '__main__':
    pass

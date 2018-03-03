import unittest

from parameterized import parameterized
from pe010_summation_of_primes.pe010 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [10, 17],
        [2000000, 142913828922]
    ])
    def test_solve(self, limit, expected_sum):
        calculated_sum = Solution().solve(limit)
        self.assertEqual(
            calculated_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, calculated_sum))


if __name__ == '__main__':
    pass

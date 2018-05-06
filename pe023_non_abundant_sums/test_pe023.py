import unittest

from parameterized import parameterized
from pe023_non_abundant_sums.pe023 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [28123, 4301608]])
    def test_solve(self, limit, expected_sum):
        returned_sum = Solution(limit).solve()
        self.assertEqual(
            returned_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, returned_sum))


if __name__ == '__main__':
    pass

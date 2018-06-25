import unittest

from parameterized import parameterized
from pe023_non_abundant_sums.pe023 import Solution
from pe023_non_abundant_sums.pe023 import Divisors


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [28123, 4301608]])
    def test_solve(self, limit, expected_sum):
        actual_sum = Solution(limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            'Failed for the limit %d.'
            % limit)


class DivisorsTest(unittest.TestCase):
    @parameterized.expand([
        [9, [1, 3]],
        [10, [1, 2, 5]],
        [12, [1, 2, 3, 4, 6]],
        [28, [1, 2, 4, 7, 14]],
        [100, [1, 2, 4, 5, 10, 20, 25, 50]]])
    def test_get_divisors(self, number, expected_divisors):
        actual_divisors = Divisors().get_divisors(number)
        self.assertEqual(
            expected_divisors,
            actual_divisors,
            'Failed for the number %d.'
            % number)


if __name__ == '__main__':
    pass

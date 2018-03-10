import unittest

from parameterized import parameterized
from pe020_factorial_digit_sum.pe020 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [10, 27],
        [100, 648]
    ])
    def test_solve(self, number, expected_sum):
        calculated_sum = Solution().solve(number)
        self.assertEqual(
            calculated_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, calculated_sum))


if __name__ == '__main__':
    pass

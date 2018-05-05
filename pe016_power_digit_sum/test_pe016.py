import unittest

from parameterized import parameterized
from pe016_power_digit_sum.pe016 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [15, 26],
        [1000, 1366]])
    def test_solve(self, power, expected_sum):
        returned_sum = Solution(power).solve()
        self.assertEqual(
            returned_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, returned_sum))


if __name__ == '__main__':
    pass

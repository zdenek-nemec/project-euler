import unittest

from parameterized import parameterized
from pe006_sum_square_difference.pe006 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [10, 2640],
        [100, 25164150]])
    def test_solve(self, number_limit, expected_difference):
        returned_difference = Solution(number_limit).solve()
        self.assertEqual(
            returned_difference,
            expected_difference,
            'The result should be %d but is %d.'
            % (expected_difference, returned_difference))


if __name__ == '__main__':
    pass

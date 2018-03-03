import unittest

from parameterized import parameterized
from pe013_large_sum.pe013 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['numbers.txt', 5537376230]
    ])
    def test_solve(self, input_filename, expected_sum):
        calculated_sum = Solution().solve(input_filename)
        self.assertEqual(
            calculated_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, calculated_sum))


if __name__ == '__main__':
    pass

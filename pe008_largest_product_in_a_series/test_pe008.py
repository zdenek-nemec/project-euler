import unittest

from parameterized import parameterized
from pe008_largest_product_in_a_series.pe008 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['number.txt', 4, 5832],
        ['number.txt', 13, 23514624000]
    ])
    def test_solve(self, input_filename, digits, expected_product):
        product = Solution().solve(input_filename, digits)
        self.assertEqual(
            product,
            expected_product,
            'The result should be %d but is %d.'
            % (expected_product, product))


if __name__ == '__main__':
    pass

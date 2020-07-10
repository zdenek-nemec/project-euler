import unittest

from parameterized import parameterized
from pe008_largest_product_in_a_series.pe008 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['number.txt', 4, 5832],
        ['number.txt', 13, 23514624000]])
    def test_solve(self, input_filename, digits, expected_product):
        returned_product = Solution(input_filename, digits).solve()
        self.assertEqual(
            returned_product,
            expected_product,
            'The result should be %d but is %d.'
            % (expected_product, returned_product))


if __name__ == '__main__':
    pass

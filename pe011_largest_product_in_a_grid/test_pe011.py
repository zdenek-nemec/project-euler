import unittest

from parameterized import parameterized
from pe011_largest_product_in_a_grid.pe011 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['numbers.csv', 4, 70600674]
    ])
    def test_solve(self, input_filename, sequence, expected_product):
        calculated_product = Solution().solve(input_filename, sequence)
        self.assertEqual(
            calculated_product,
            expected_product,
            'The result should be %d but is %d.'
            % (expected_product, calculated_product))


if __name__ == '__main__':
    pass

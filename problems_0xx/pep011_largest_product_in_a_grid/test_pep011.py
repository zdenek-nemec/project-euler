import unittest

from parameterized import parameterized
from pe011_largest_product_in_a_grid.pe011 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['numbers.csv', 4, 70600674]])
    def test_solve(self, input_filename, sequence, expected_product):
        returned_product = Solution(input_filename, sequence).solve()
        self.assertEqual(
            returned_product,
            expected_product,
            'The result should be %d but is %d.'
            % (expected_product, returned_product))


if __name__ == '__main__':
    pass

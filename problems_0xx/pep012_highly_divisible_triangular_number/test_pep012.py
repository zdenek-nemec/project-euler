import unittest

from parameterized import parameterized
from pe012_highly_divisible_triangular_number.pe012 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [5, 28],
        [500, 76576500]])
    def test_solve(self, divisors_limit, expected_triangle_number):
        returned_triangle_number = Solution(divisors_limit).solve()
        self.assertEqual(
            returned_triangle_number,
            expected_triangle_number,
            'The result should be %d but is %d.'
            % (expected_triangle_number, returned_triangle_number))


if __name__ == '__main__':
    pass
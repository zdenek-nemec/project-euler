import unittest

from parameterized import parameterized
from pe005_smallest_multiple.pe005 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [10, 2520],
        [20, 232792560]
    ])
    def test_solve(self, divisor_limit, expected_number):
        returned_number = Solution(divisor_limit).solve()
        self.assertEqual(
            returned_number,
            expected_number,
            'The result should be %d but is %d.'
            % (expected_number, returned_number))


if __name__ == '__main__':
    pass

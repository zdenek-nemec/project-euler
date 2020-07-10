import unittest

from parameterized import parameterized
from pe018_maximum_path_sum_i.pe018 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['triangle_small.txt', 23],
        ['triangle_big.txt', 1074]])
    def test_solve(self, input_filename, expected_total):
        returned_total = Solution(input_filename).solve()
        self.assertEqual(
            returned_total,
            expected_total,
            'The result should be %d but is %d.'
            % (expected_total, returned_total))


if __name__ == '__main__':
    pass

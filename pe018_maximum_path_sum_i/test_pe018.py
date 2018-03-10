import unittest

from parameterized import parameterized
from pe018_maximum_path_sum_i.pe018 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['triangle_small.txt', 23],
        ['triangle_big.txt', 1074]
    ])
    def test_solve(self, input_filename, expected_total):
        calculated_total = Solution().solve(input_filename)
        self.assertEqual(
            calculated_total,
            expected_total,
            'The result should be %d but is %d.'
            % (expected_total, calculated_total))


if __name__ == '__main__':
    pass

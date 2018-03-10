import unittest

from parameterized import parameterized
from pe022_names_scores.pe022 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['p022_names.txt', 871198282]
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

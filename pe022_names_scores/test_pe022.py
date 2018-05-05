import unittest

from parameterized import parameterized
from pe022_names_scores.pe022 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['p022_names.txt', 871198282]])
    def test_solve(self, input_filename, expected_total):
        returned_total = Solution(input_filename).solve()
        self.assertEqual(
            returned_total,
            expected_total,
            'The result should be %d but is %d.'
            % (expected_total, returned_total))


if __name__ == '__main__':
    pass

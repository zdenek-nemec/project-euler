import unittest

from parameterized import parameterized
from pe017_number_letter_counts.pe017 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [5, 19],
        [1000, 21124]
    ])
    def test_solve(self, top, expected_letters):
        calculated_letters = Solution().solve(top)
        self.assertEqual(
            calculated_letters,
            expected_letters,
            'The result should be %d but is %d.'
            % (expected_letters, calculated_letters))


if __name__ == '__main__':
    pass

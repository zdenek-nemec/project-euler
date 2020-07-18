import unittest

from parameterized import parameterized
from pe014_longest_collatz_sequence.pe014 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [1000000, 837799]])
    def test_solve(self, limit, expected_number):
        returned_number = Solution(limit).solve()
        self.assertEqual(
            returned_number,
            expected_number,
            'The result should be %d but is %d.'
            % (expected_number, returned_number))


if __name__ == '__main__':
    pass
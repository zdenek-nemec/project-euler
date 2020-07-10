import unittest

from parameterized import parameterized
from pe019_counting_sundays.pe019 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [
            (1900, 1, 1, 'Monday'),
            (0, 0, 1, 'Sunday'),
            (1901, 1, 1),
            (2000, 12, 31),
            171]])
    def test_solve(self, seed, search, start, end, expected_number):
        returned_number = Solution(seed, search, start, end).solve()
        self.assertEqual(
            returned_number,
            expected_number,
            'The result should be %d but is %d.'
            % (expected_number, returned_number))


if __name__ == '__main__':
    pass

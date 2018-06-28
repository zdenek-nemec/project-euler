import unittest

from parameterized import parameterized

from pe025_1000_digit_fibonacci_number.pe025 import Solution


class TestSolutionMethods(unittest.TestCase):
    @parameterized.expand([
        [3, [1, 1], 12],
        [1000, [1, 1], 4782]])
    def test_solve(self, digits, start, expected_index):
        actual_index = Solution(digits, start).solve()
        self.assertEqual(
            expected_index,
            actual_index,
            'Failed for %d digits.'
            % digits)


if __name__ == '__main__':
    unittest.main()

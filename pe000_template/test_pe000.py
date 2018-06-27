import unittest

from parameterized import parameterized

from pe000_template.pe000 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [3, 3],
        [7, 7]])
    def test_solve(self, lucky_number, expected_lucky_number):
        actual_lucky_number = Solution(lucky_number).solve()
        self.assertEqual(
            expected_lucky_number,
            actual_lucky_number,
            'Failed for the number %d.'
            % lucky_number)


if __name__ == '__main__':
    pass

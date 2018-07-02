import unittest

from parameterized import parameterized

from pe026_reciprocal_cycles.pe026 import Solution
from pe026_reciprocal_cycles.pe026 import Dividend


class TestSolutionMethods(unittest.TestCase):
    @parameterized.expand([
        [10, 7]
    ])
    def test_solve(self, limit, expected_denominator):
        actual_denominator = Solution(limit).solve()
        self.assertEqual(
            expected_denominator,
            actual_denominator,
            'Failed for limit %d.'
            % limit
        )


class TestDividendMethods(unittest.TestCase):
    @parameterized.expand([
        [2, []],
        [3, [3]],
        [4, []],
        [5, []],
        [6, [6]],
        [7, [1, 4, 2, 8, 5, 7]],
        [8, []],
        [9, [1]]
    ])
    def test_cycle(self, denominator, expected_cycle):
        dividend = Dividend(1, denominator)
        dividend.calculate()
        actual_cycle = dividend.get_cycle()
        self.assertEqual(
            expected_cycle,
            actual_cycle,
            'Failed for denominator %d.'
            % denominator
        )

    @parameterized.expand([
        [2, [0, 5]],
        [3, [0, 3, 3]],
        [4, [0, 2, 5]],
        [5, [0, 2]],
        [6, [0, 1, 6, 6]],
        [7, [0, 1, 4, 2, 8, 5, 7, 1, 4, 2, 8, 5, 7]],
        [8, [0, 1, 2, 5]],
        [9, [0, 1, 1]]
    ])
    def test_dividend(self, denominator, expected_dividend):
        dividend = Dividend(1, denominator)
        dividend.calculate()
        actual_dividend = dividend.get_dividend()
        self.assertEqual(
            expected_dividend,
            actual_dividend,
            'Failed for denominator %d.'
            % denominator
        )


if __name__ == '__main__':
    unittest.main()

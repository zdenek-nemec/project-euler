import unittest

from parameterized import parameterized

from pe026_reciprocal_cycles.pe026 import Solution


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


if __name__ == '__main__':
    unittest.main()

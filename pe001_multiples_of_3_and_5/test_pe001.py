import unittest

from parameterized import parameterized
from pe001_multiples_of_3_and_5.pe001 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[3, 5], 10, 23],
        [[3, 5], 1000, 233168]
    ])
    def test_solve(self, multipliers, limit, expected_sum):
        sum_of_multiples = Solution().solve(multipliers, limit)
        self.assertEqual(
            sum_of_multiples,
            expected_sum,
            "The result should be %d but is %d."
            % (expected_sum, sum_of_multiples))


if __name__ == "__main__":
    pass

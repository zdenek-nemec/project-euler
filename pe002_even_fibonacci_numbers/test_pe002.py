import unittest

from parameterized import parameterized
from pe002_even_fibonacci_numbers.pe002 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [[1, 2], 4000000, 4613732]
    ])
    def test_solve(self, start, limit, expected_sum):
        sum_of_even = Solution.solve(start, limit)
        self.assertEqual(
            sum_of_even,
            expected_sum,
            "The result should be %d but is %d."
            % (expected_sum, sum_of_even))


if __name__ == "__main__":
    pass

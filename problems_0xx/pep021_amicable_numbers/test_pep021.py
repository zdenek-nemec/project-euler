import unittest

from parameterized import parameterized
from pe021_amicable_numbers.pe021 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [10000, 31626]])
    def test_solve(self, limit, expected_sum):
        returned_sum = Solution(limit).solve()
        self.assertEqual(
            returned_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, returned_sum))


if __name__ == '__main__':
    pass

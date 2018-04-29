import unittest

from parameterized import parameterized
from pe013_large_sum.pe013 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['numbers.txt', 5537376230]])
    def test_solve(self, input_filename, expected_sum):
        returned_sum = Solution(input_filename).solve()
        self.assertEqual(
            returned_sum,
            expected_sum,
            'The result should be %d but is %d.'
            % (expected_sum, returned_sum))


if __name__ == '__main__':
    pass

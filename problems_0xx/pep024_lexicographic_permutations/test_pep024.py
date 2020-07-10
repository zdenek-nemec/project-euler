import unittest

from parameterized import parameterized
from pe024_lexicographic_permutations.pe024 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        ['012', 1, '012'],
        ['0123456789', 1000000, '2783915460']])
    def test_solve(self, characters, position, expected_permutation):
        returned_permutation = Solution(characters, position).solve()
        self.assertEqual(
            returned_permutation,
            expected_permutation,
            'The result should be %s but is %s.'
            % (expected_permutation, returned_permutation))


if __name__ == '__main__':
    pass

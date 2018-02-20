import unittest

from parameterized import parameterized
from pe004_largest_palindrome_product.pe004 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [2, 9009],
        [3, 906609]
    ])
    def test_solve(self, digits, expected_palindrome):
        palindrome = Solution().solve(digits)
        self.assertEqual(
            palindrome,
            expected_palindrome,
            "The result should be %d but is %d."
            % (expected_palindrome, palindrome))


if __name__ == "__main__":
    pass

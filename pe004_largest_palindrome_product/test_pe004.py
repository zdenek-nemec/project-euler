import unittest

from parameterized import parameterized
from pe004 import SolutionTopToBottom


class SolutionTopToBottomTest(unittest.TestCase):
    @parameterized.expand([
        [2, 9009],
        [3, 906609]
    ])
    def test_solution(self, digits, expected_palindrome):
        palindrome = SolutionTopToBottom().solve(digits)
        self.assertEqual(
            palindrome,
            expected_palindrome,
            "Result should be %d but is %d." %
            (expected_palindrome, palindrome)
        )


if __name__ == "__main__":
    pass

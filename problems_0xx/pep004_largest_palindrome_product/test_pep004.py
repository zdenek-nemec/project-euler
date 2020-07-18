import unittest

from parameterized import parameterized

from problems_0xx.pep004_largest_palindrome_product.pep004 import ProjectEulerProblem004


class ProjectEulerProblem004Test(unittest.TestCase):
    @parameterized.expand([
        [2, 9009],
        [3, 906609]])
    def test_solve(self, digits, expected_palindrome):
        actual_palindrome = ProjectEulerProblem004(digits).solve()
        self.assertEqual(
            expected_palindrome,
            actual_palindrome,
            "Failed for %d digits."
            % digits)


if __name__ == "__main__":
    unittest.main()

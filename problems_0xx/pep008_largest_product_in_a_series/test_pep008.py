import unittest

from parameterized import parameterized

from problems_0xx.pep008_largest_product_in_a_series.pep008 import ProjectEulerProblem008


class ProjectEulerProblem008Test(unittest.TestCase):
    @parameterized.expand([
        ["number.txt", 4, 5832],
        ["number.txt", 13, 23514624000]])
    def test_solve(self, input_filename, digits, expected_product):
        actual_product = ProjectEulerProblem008(input_filename, digits).solve()
        self.assertEqual(
            expected_product,
            actual_product,
            "Failed for %d digits."
            % digits)


if __name__ == "__main__":
    unittest.main()

import unittest

from parameterized import parameterized

from problems_0xx.pep011_largest_product_in_a_grid.pep011 import ProjectEulerProblem011


class ProjectEulerProblem011Test(unittest.TestCase):
    @parameterized.expand([
        ["numbers.csv", 4, 70600674]])
    def test_solve(self, input_filename, sequence, expected_product):
        actual_product = ProjectEulerProblem011(input_filename, sequence).solve()
        self.assertEqual(
            expected_product,
            actual_product,
            "Actual and expected products do not match.")


if __name__ == "__main__":
    unittest.main()

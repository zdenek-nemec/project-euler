import unittest

from parameterized import parameterized

from problems_0xx.pep013_large_sum.pep013 import ProjectEulerProblem013


class ProjectEulerProblem013Test(unittest.TestCase):
    @parameterized.expand([
        ["numbers.txt", 5537376230]])
    def test_solve(self, input_filename, expected_sum):
        actual_sum = ProjectEulerProblem013(input_filename).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Actual and expected sums do not match.")


if __name__ == "__main__":
    unittest.main()

import unittest

from parameterized import parameterized

from problems_0xx.pep022_names_scores.pep022 import ProjectEulerProblem022


class ProjectEulerProblem022Test(unittest.TestCase):
    @parameterized.expand([
        ["p022_names.txt", 871198282]])
    def test_solve(self, input_filename, expected_total):
        actual_total = ProjectEulerProblem022(input_filename).solve()
        self.assertEqual(
            expected_total,
            actual_total,
            "Expected and actual totals do not match.")


if __name__ == "__main__":
    unittest.main()

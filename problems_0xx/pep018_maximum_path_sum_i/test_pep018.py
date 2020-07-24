import unittest

from parameterized import parameterized

from problems_0xx.pep018_maximum_path_sum_i.pep018 import ProjectEulerProblem018


class ProjectEulerProblem018Test(unittest.TestCase):
    @parameterized.expand([
        ["triangle_small.txt", 23],
        ["triangle_big.txt", 1074]])
    def test_solve(self, input_filename, expected_total):
        actual_total = ProjectEulerProblem018(input_filename).solve()
        self.assertEqual(
            expected_total,
            actual_total,
            "Failed for the file %s."
            % input_filename)


if __name__ == "__main__":
    unittest.main()

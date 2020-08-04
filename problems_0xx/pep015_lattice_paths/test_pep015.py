import unittest

from parameterized import parameterized

from problems_0xx.pep015_lattice_paths.pep015 import ProjectEulerProblem015


class ProjectEulerProblem015Test(unittest.TestCase):
    @parameterized.expand([
        [2, 2, 6],
        [20, 20, 137846528820]])
    def test_solve(self, size_x, size_y, expected_paths):
        actual_paths = ProjectEulerProblem015(size_x, size_y).solve()
        self.assertEqual(
            expected_paths,
            actual_paths,
            "Failed for grid %dx%d."
            % (size_x, size_y))


if __name__ == "__main__":
    unittest.main()

import unittest

from parameterized import parameterized

from problems_0xx.pep009_special_pythagorean_triplet.pep009 import ProjectEulerProblem009


class ProjectEulerProblem009Test(unittest.TestCase):
    @parameterized.expand([
        [12, 60],
        [1000, 31875000]])
    def test_solve(self, target_sum, expected_product):
        actual_product = ProjectEulerProblem009(target_sum).solve()
        self.assertEqual(
            expected_product,
            actual_product,
            "Failed for target sum %d."
            % target_sum)


if __name__ == "__main__":
    unittest.main()

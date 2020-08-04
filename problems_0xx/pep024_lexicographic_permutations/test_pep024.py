import unittest

from parameterized import parameterized

from problems_0xx.pep024_lexicographic_permutations.pep024 import ProjectEulerProblem024


class ProjectEulerProblem024Test(unittest.TestCase):
    @parameterized.expand([
        ["012", 1, "012"],
        ["0123456789", 1000000, "2783915460"]])
    def test_solve(self, characters, position, expected_permutation):
        returned_permutation = ProjectEulerProblem024(characters, position).solve()
        self.assertEqual(
            expected_permutation,
            returned_permutation,
            "Failed for characters %s and position %d."
            % (characters, position))


if __name__ == "__main__":
    unittest.main()

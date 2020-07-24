import unittest

from parameterized import parameterized

from problems_0xx.pep017_number_letter_counts.pep017 import ProjectEulerProblem017


class ProjectEulerProblem017Test(unittest.TestCase):
    @parameterized.expand([
        [5, 19],
        [1000, 21124]])
    def test_solve(self, top, expected_letters):
        actual_letters = ProjectEulerProblem017(top).solve()
        self.assertEqual(
            expected_letters,
            actual_letters,
            "Failed for top of %d."
            % top)


if __name__ == "__main__":
    unittest.main()

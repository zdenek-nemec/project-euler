import unittest

from parameterized import parameterized

from problems_0xx.pep019_counting_sundays.pep019 import ProjectEulerProblem019


class ProjectEulerProblem019Test(unittest.TestCase):
    @parameterized.expand([
        [
            (1900, 1, 1, "Monday"),
            (0, 0, 1, "Sunday"),
            (1901, 1, 1),
            (2000, 12, 31),
            171]])
    def test_solve(self, seed, search, start, end, expected_number):
        actual_number = ProjectEulerProblem019(seed, search, start, end).solve()
        self.assertEqual(
            expected_number,
            actual_number,
            "Expected and actual numbers do not match.")


if __name__ == "__main__":
    unittest.main()

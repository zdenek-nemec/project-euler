import unittest

from parameterized import parameterized

from problems_0xx.pep023_non_abundant_sums.pep023 import Divisors
from problems_0xx.pep023_non_abundant_sums.pep023 import ProjectEulerProblem023A
from problems_0xx.pep023_non_abundant_sums.pep023 import ProjectEulerProblem023B


class ProjectEulerProblem023ATest(unittest.TestCase):
    @parameterized.expand([
        [3000, 989657]])
    def test_solve(self, limit, expected_sum):
        actual_sum = ProjectEulerProblem023A(limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Failed for the limit %d."
            % limit)


class ProjectEulerProblem023BTest(unittest.TestCase):
    @parameterized.expand([
        [3000, 989657]])
    def test_solve(self, limit, expected_sum):
        actual_sum = ProjectEulerProblem023B(limit).solve()
        self.assertEqual(
            expected_sum,
            actual_sum,
            "Failed for the limit %d."
            % limit)


class DivisorsTest(unittest.TestCase):
    @parameterized.expand([
        [9, [1, 3]],
        [10, [1, 2, 5]],
        [12, [1, 2, 3, 4, 6]],
        [28, [1, 2, 4, 7, 14]],
        [100, [1, 2, 4, 5, 10, 20, 25, 50]]])
    def test_get_divisors(self, number, expected_divisors):
        actual_divisors = Divisors().get_divisors(number)
        self.assertEqual(
            expected_divisors,
            actual_divisors,
            "Failed for the number %d."
            % number)


if __name__ == "__main__":
    unittest.main()

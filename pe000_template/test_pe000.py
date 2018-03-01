import unittest

from parameterized import parameterized
from pe000_template.pe000 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [3, 3],
        [7, 7]
    ])
    def test_solve(self, lucky_number, expected_lucky_number):
        returned_lucky_number = Solution().solve(lucky_number)
        self.assertEqual(
            returned_lucky_number,
            expected_lucky_number,
            "The result should be %d but is %d."
            % (expected_lucky_number, returned_lucky_number))


if __name__ == "__main__":
    pass

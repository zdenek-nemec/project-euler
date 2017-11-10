import unittest

from parameterized import parameterized
from pe001 import SolutionModulo


class SolutionModuloTest(unittest.TestCase):
    @parameterized.expand([
        [10, [3, 5], 23],
        [1000, [3, 5], 233168]
    ])
    def test_sum_multiples(self, limit, bases, expected_result):
        sum_of_multiples = SolutionModulo(limit).sum_multiples(bases)
        self.assertEqual(
            sum_of_multiples,
            expected_result,
            "Result should be %d but is %d."
            % (expected_result, sum_of_multiples))


if __name__ == "__main__":
    pass

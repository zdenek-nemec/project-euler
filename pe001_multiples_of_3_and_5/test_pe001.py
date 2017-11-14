import unittest

from parameterized import parameterized
from pe001 import Multiples


class MultiplesTest(unittest.TestCase):
    @parameterized.expand([
        [[3, 5], 10, 23],
        [[3, 5], 1000, 233168]
    ])
    def test_sum_multiples(self, bases, limit, expected_result):
        sum_of_multiples = Multiples(bases).sum_multiples(limit)
        self.assertEqual(
            sum_of_multiples,
            expected_result,
            "Result should be %d but is %d."
            % (expected_result, sum_of_multiples))


if __name__ == "__main__":
    pass

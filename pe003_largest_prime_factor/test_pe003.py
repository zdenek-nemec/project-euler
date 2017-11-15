import unittest

from parameterized import parameterized
from pe003 import Factors


class FactorsTest(unittest.TestCase):
    @parameterized.expand([
        [10, [2, 5]],
        [24, [2, 3, 4, 6, 8, 12]]
    ])
    def test_get_factors(self, number, expected_result):
        factors = Factors().get_factors(number)
        self.assertEqual(
            factors,
            expected_result,
            ("Result should be", expected_result, "but is", factors))

    @parameterized.expand([
        [13195, [5, 7, 13, 29]]
    ])
    def test_get_prime_factors(self, number, expected_result):
        prime_factors = Factors().get_prime_factors(number)
        self.assertEqual(
            prime_factors,
            expected_result,
            ("Result should be", expected_result, "but is", prime_factors))

    @parameterized.expand([
        [13195, 29],
        [600851475143, 6857]
    ])
    def test_get_largest_prime_factor(self, number, expected_result):
        largest_prime_factor = Factors().get_largest_prime_factor(number)
        self.assertEqual(
            largest_prime_factor,
            expected_result,
            "Result should be %d but is %d."
            % (expected_result, largest_prime_factor))


if __name__ == "__main__":
    pass

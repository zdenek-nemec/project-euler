import unittest

from parameterized import parameterized
from pe002 import Fibonacci


class FibonacciTest(unittest.TestCase):
    @parameterized.expand([
        [10, [1, 2, 3, 5, 8]],
        [100, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]]
    ])
    def test_generate_numbers(self, limit, expected_result):
        numbers = Fibonacci(limit)._generate_numbers(limit)
        self.assertEqual(
            numbers,
            expected_result,
            ("Result should be", expected_result, "but is", numbers))

    @parameterized.expand([
        [[1, 2], 3],
        [[1, 2, 3], 5],
        [[1, 2, 3, 5], 8],
        [[1, 2, 3, 5, 8], 13]
    ])
    def test_get_next(self, numbers, expected_result):
        next_number = Fibonacci.get_next(numbers)
        self.assertEqual(
            next_number,
            expected_result,
            "Result should be %d but is %d."
            % (expected_result, next_number))

    @parameterized.expand([
        [4000000, 4613732]
    ])
    def test_sum_even(self, limit, expected_result):
        sum_of_even = Fibonacci(limit).sum_even()
        self.assertEqual(
            sum_of_even,
            expected_result,
            "Result should be %d but is %d."
            % (expected_result, sum_of_even))


if __name__ == "__main__":
    pass

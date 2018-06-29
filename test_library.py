import unittest

from parameterized import parameterized

from library import Divisors
from library import Fibonacci


class TestDivisorsMethods(unittest.TestCase):
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
            'Failed for the number %d.'
            % number)


class TestFibonacciMethods(unittest.TestCase):
    @parameterized.expand([
        [[1, 1], 3, 2],
        [[1, 1], 4, 3],
        [[1, 1], 5, 5],
        [[1, 1], 6, 8],
        [[1, 1], 7, 13]])
    def test_append_next(self, start, length, expected_last):
        fibonacci = Fibonacci(start)
        while fibonacci.get_length() < length:
            fibonacci.append_next()
        actual_last = fibonacci.get_last()
        self.assertEqual(
            expected_last,
            actual_last,
            'Failed for start %s and length %d.'
            % (str(start), length)
        )


if __name__ == '__main__':
    unittest.main()

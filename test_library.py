import unittest

from parameterized import parameterized

from library import Divisors


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
            'Failed for the number %d.'
            % number)


if __name__ == '__main__':
    pass

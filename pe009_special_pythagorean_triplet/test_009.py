import unittest

from parameterized import parameterized
from pe009_special_pythagorean_triplet.pe009 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [12, 60],
        [1000, 31875000]
    ])
    def test_solve(self, target_sum, expected_product):
        product = Solution().solve(target_sum)
        self.assertEqual(
            product,
            expected_product,
            'The result should be %d but is %d.'
            % (expected_product, product))


if __name__ == '__main__':
    pass

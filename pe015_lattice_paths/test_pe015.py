import unittest

from parameterized import parameterized
from pe015_lattice_paths.pe015 import Solution


class SolutionTest(unittest.TestCase):
    @parameterized.expand([
        [2, 2, 6],
        [20, 20, 137846528820]
    ])
    def test_solve(self, size_x, size_y, expected_paths):
        calculated_paths = Solution().solve(size_x, size_y)
        self.assertEqual(
            calculated_paths,
            expected_paths,
            'The result should be %d but is %d.'
            % (expected_paths, calculated_paths))


if __name__ == '__main__':
    pass

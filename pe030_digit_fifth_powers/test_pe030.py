#!/usr/bin/env python3


import unittest
import parameterized

from pe030 import Solution030


class Solution030Test(unittest.TestCase):
    @parameterized.parameterized.expand([
        [3, 3],
        [7, 7]])
    def test_solve(self, number, expected_result):
        actual_result = Solution030(number).solve()
        self.assertEqual(
            actual_result,
            expected_result,
            "Failed for the number %d."
            % number)


if __name__ == "__main__":
    unittest.main()

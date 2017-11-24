#!/usr/bin/env python3

"""
PE001: Multiples of 3 and 5
---------------------------

Name: pe001.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 3.1 (2017-11-24)

Synopsis:
    ``pe001.py``

Examples:
    ``pe001.py``

Description:
    Solution for Project Euler problem 1 (https://projecteuler.net/problem=1).

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""


MULTIPLIERS = [3, 5]
LIMIT = 1000


class Solution(object):
    @staticmethod
    def solve(multipliers, limit):
        sum_of_multiples = 0
        for number in range(limit):
            for selected_multiplier in multipliers:
                if number % selected_multiplier == 0:
                    sum_of_multiples += number
                    break
        return sum_of_multiples


def main():
    print(Solution.solve(MULTIPLIERS, LIMIT))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
PE005: Smallest multiple
------------------------

Name: pe005.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.1 (2018-02-25)

Synopsis:
    ``pe005.py``

Examples:
    ``pe005.py``

Description:
    Solution for Project Euler Problem 5 (https://projecteuler.net/problem=5).

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
"""


TOP = 20


class Solution(object):
    @staticmethod
    def get_seed(top):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
        seed = 1
        for prime in prime_list:
            if prime < top:
                seed *= prime
        return seed

    @staticmethod
    def check_divisibility(number, top):
        for divisor in range(top, 1, -1):
            if (number % divisor) != 0:
                return False
        return True

    @staticmethod
    def solve(top):
        seed = Solution().get_seed(top)
        number = seed
        while True:
            number += seed
            if Solution().check_divisibility(number, top):
                break
        return number


def main():
    print(Solution().solve(TOP))


if __name__ == "__main__":
    main()

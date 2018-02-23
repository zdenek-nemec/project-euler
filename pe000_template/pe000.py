#!/usr/bin/env python3

"""
PE000: Template
---------------

Name: pe000.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2018-00-00)

Synopsis:
    ``pe000.py``

Examples:
    ``pe000.py``

Description:
    Solution for Project Euler Problem 0
    (https://projecteuler.net/problem=0).

    This is just a template.
"""


LUCKY_NUMBER = 7


class Solution(object):
    @staticmethod
    def solve(lucky_number):
        return lucky_number


def main():
    print(Solution.solve(LUCKY_NUMBER))


if __name__ == "__main__":
    main()

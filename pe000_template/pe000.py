#!/usr/bin/env python3

"""
PE-000: Template
----------------

Solution for Project Euler Problem 0 (https://projecteuler.net/problem=0).

This is just a template.

.. warning:: Open
"""


LUCKY_NUMBER = 7


class Solution(object):
    def __init__(self, lucky_number):
        self._lucky_number = lucky_number

    def solve(self):
        return self._lucky_number


def main():
    print(Solution(LUCKY_NUMBER).solve())


if __name__ == '__main__':
    main()

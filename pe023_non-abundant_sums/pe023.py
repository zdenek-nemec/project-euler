#!/usr/bin/env python3

"""
PE-023: Non-abundant sums
-------------------------

Solution for Project Euler Problem 23 (https://projecteuler.net/problem=23).

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
:math:`1 + 2 + 4 + 7 + 14 = 28`, which means that 28 is a perfect number.

A number :math:`n` is called deficient if the sum of its proper divisors is less
than :math:`n` and it is called abundant if this sum exceeds :math:`n`.

As 12 is the smallest abundant number, :math:`1 + 2 + 3 + 4 + 6 = 16`, the
smallest number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

.. warning:: Open
"""


class Solution(object):
    @staticmethod
    def solve():
        return 0


def main():
    print(Solution().solve())


if __name__ == '__main__':
    main()

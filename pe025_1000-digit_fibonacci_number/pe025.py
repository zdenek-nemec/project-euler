#!/usr/bin/env python3

"""
PE-025: 1000-digit Fibonacci number
-----------------------------------

Solution for Project Euler Problem 25 (https://projecteuler.net/problem=25).

The Fibonacci sequence is defined by the recurrence relation:

:math:`F_{n} = F_{n-1} + F_{n-2}`, where :math:`F_1 = 1` and
:math:`F_2 = 1`.

Hence the first 12 terms will be:

.. math::

    F_{1} &= 1

    F_{2} &= 1

    F_{3} &= 2

    F_{4} &= 3

    F_{5} &= 5

    F_{6} &= 8

    F_{7} &= 13

    F_{8} &= 21

    F_{9} &= 34

    F_{10} &= 55

    F_{11} &= 89

    F_{12} &= 144

..

The 12th term, :math:`F_12`, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?

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

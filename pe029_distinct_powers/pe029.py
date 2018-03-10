#!/usr/bin/env python3

"""
PE-029: Distinct powers
-----------------------

Solution for Project Euler Problem 29 (https://projecteuler.net/problem=29).

Consider all integer combinations of :math:`a^b` for :math:`2 \leq a \leq 5` and
:math:`2 \leq b \leq 5`:

:math:`2^2=4, 2^3=8, 2^4=16, 2^5=32`

:math:`3^2=9, 3^3=27, 3^4=81, 3^5=343`

:math:`4^2=16, 4^3=64, 4^4=256, 4^5=1024`

:math:`5^2=25, 5^3=125, 5^4=625, 5^5=3125`

If they are then placed in numerical order, with any repeats removed, we get the
following sequence of 15 distinct terms:

:math:`4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125`

How many distinct terms are in the sequence generated by :math:`a^b` for
:math:`2 \leq a \leq 100` and :math:`2 \leq b \leq 100`?

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

#!/usr/bin/env python3

"""
PE-026: Reciprocal cycles
-------------------------

Solution for Project Euler Problem 26 (https://projecteuler.net/problem=26).

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

.. math::

    1/2 &= 0.5

    1/3 &= 0.(3)

    1/4 &= 0.25

    1/5 &= 0.2

    1/6 &= 0.1(6)

    1/7 &= 0.(142857)

    1/8 &= 0.125

    1/9 &= 0.(1)

    1/10 &= 0.1

..

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of :math:`d<1000` for which :math:`1/d` contains the longest
recurring cycle in its decimal fraction part.

.. warning:: Open
"""


LIMIT = 10


class Solution(object):
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        print(self._limit)
        for denominator in range(2, self._limit):
            print('1 / %d = %f' % (denominator, 1 / denominator))
        return 7


if __name__ == '__main__':
    print(Solution(LIMIT).solve())

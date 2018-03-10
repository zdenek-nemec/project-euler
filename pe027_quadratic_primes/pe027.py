#!/usr/bin/env python3

"""
PE-027: Quadratic primes
------------------------

Solution for Project Euler Problem 27 (https://projecteuler.net/problem=27).

Euler discovered the remarkable quadratic formula:

:math:`n^2 + n + 41`

It turns out that the formula will produce 40 primes for the consecutive integer
values :math:`0 \leq n \leq 39`. However, when
:math:`n = 40, 40^2 + 40 + 41 = 40 (40 + 1) + 41` is divisible by 41, and
certainly when :math:`n = 41, 41^2 + 41 + 41` is clearly divisible by 41.

The incredible formula :math:`n^2 - 79n + 1601` was discovered, which produces
80 primes for the consecutive values :math:`0 \leq n \leq 79`. The product of
the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

:math:`n^2 + an + b`, where :math:`|a| \lt 1000` and :math:`|b| \leq 1000`

where :math:`|n|` is the modulus/absolute value of :math:`n`

e.g. :math:`|11| = 11` and :math:`|-4| = 4`

Find the product of the coefficients, :math:`a` and :math:`b`, for the quadratic
expression that produces the maximum number of primes for consecutive values of
:math:`n`, starting with :math:`n = 0`.

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

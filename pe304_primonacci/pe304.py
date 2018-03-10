#!/usr/bin/env python3

"""
PE-304: Primonacci
------------------

Solution for Project Euler Problem 304 (https://projecteuler.net/problem=304).

For any positive integer :math:`n` the function :math:`\\text{next_prime}(n)`
returns the smallest prime :math:`p` such that :math:`p > n`.

The sequence :math:`a(n)` is defined by:
:math:`a(1) = \\text{next_prime}(10^{14})` and
:math:`a(n) = \\text{next_prime}(a(n-1))` for :math:`n>1`.

The fibonacci sequence :math:`f(n)` is defined by: :math:`f(0) = 0, f(1) = 1`
and :math:`f(n) = f(n-1) + f(n-2)` for :math:`n>1`.

The sequence :math:`b(n)` is defined as :math:`f(a(n))`.

Find :math:`\sum b(n)` for :math:`1 \leq n \leq 100000`. Give your answer
:math:`\\text{mod }1234567891011`.

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

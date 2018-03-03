#!/usr/bin/env python3

"""
PE-009: Special Pythagorean triplet
-----------------------------------

Solution for Project Euler Problem 9 (https://projecteuler.net/problem=9).

A Pythagorean triplet is a set of three natural numbers, :math:`a < b < c`, for
which,

.. math::

    a^2 + b^2 = c^2

..

For example, :math:`3^2 + 4^2 = 9 + 16 = 25 = 5^2`.

There exists exactly one Pythagorean triplet for which :math:`a + b + c = 1000`.
Find the product :math:`abc`.
"""


TARGET_SUM = 1000


class Solution(object):
    @staticmethod
    def solve(target_sum):
        """
        Pre-calculate array of second powers. Then search for sum of
        :math:`a^2 + b^2` which is in the array. Upon finding such set, check
        sum of a, b and c. If it matches, return product of a, b and c.
        """
        powers = [0]
        for number in range(1, target_sum + 1):
            powers.append(number ** 2)
        for a in range(1, target_sum + 1):
            for b in range(a + 1, target_sum - a):
                cc = powers[a] + powers[b]
                if cc in powers:
                    if a + b + powers.index(cc) == target_sum:
                        return a * b * powers.index(cc)
        return -1


def main():
    print(Solution().solve(TARGET_SUM))


if __name__ == '__main__':
    main()

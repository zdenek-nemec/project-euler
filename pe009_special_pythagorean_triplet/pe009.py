#!/usr/bin/env python3

"""
PE009: Special Pythagorean triplet
----------------------------------

Name: pe009.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe009.py``

Examples:
    ``pe009.py``

Description:
    Solution for Project Euler Problem 9 (https://projecteuler.net/problem=9).

    A Pythagorean triplet is a set of three natural numbers,
    :math:`a < b < c`, for which,

.. math::

    a^2 + b^2 = c^2

..

    For example, :math:`3^2 + 4^2 = 9 + 16 = 25 = 5^2`.

    There exists exactly one Pythagorean triplet for which
    :math:`a + b + c = 1000`. Find the product :math:`abc`.
"""


SUM = 1000


# Solution: Power Array #######################################################

def solve_power_array(sum):
    """
    Pre-calculate array of second powers. Then search for sum of
    :math:`a^2 + b^2` which is in the array. Upon finding such set, check sum
    of a, b, and c.
    """
    powers = [0]
    for i in range(1, sum+1):
        powers.append(i ** 2)
    for a in range(1, sum+1):
        for b in range(a+1, sum-a):
            cc = powers[a] + powers[b]
            if (cc in powers):
                # print a, b, powers.index(cc)
                if ((a + b + powers.index(cc)) == sum):
                    return (a * b * powers.index(cc))
    return -1


# Main ########################################################################

def main():
    result = solve_power_array(SUM)
    print("Solution: Power Array")
    print("\tThe product of Pythagorean triplet which sum is", SUM,"is", result)
    return 0


if __name__ == "__main__":
    main()

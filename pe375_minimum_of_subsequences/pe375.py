#!/usr/bin/env python

"""
PE375: Minimum of subsequences
------------------------------

Name: pe375.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-06-12)

Synopsis:
    ``pe375.py``

Examples:
    ``pe375.py``

Description:
    Solution for Project Euler Problem 375
    (https://projecteuler.net/problem=375).

    Let :math:`S_{n}` be an integer sequence produced with the following
    pseudo-random number generator:

.. math::

    S_{0} &= 290797

    S_{n+1} &= {S_{n}}^{2} \\text{ mod } 50515093

..

    Let :math:`A(i,j)` be the minimum of the numbers
    :math:`S_{i}, S_{i+1}, ..., S_{j}` for :math:`i \\leq j`.

    Let :math:`M(N) = \\sum A(i,j)` for :math:`1 \\leq i \\leq j \\leq N`.

    We can verify that :math:`M(10) = 432256955` and
    :math:`M(10 \\ 000) = 3264567774119`.

    Find :math:`M(2 \\ 000 \\ 000 \\ 000)`.
"""


import sys


LUCKY_NUMBER = 7


# Solution: Brute Force #######################################################

class LuckyNumbers():
    def __init__(self):
        self.current_number = LUCKY_NUMBER

    def assign_lucky_number(self, number):
        self.current_number = number
        return 0

    def get_current_number(self):
        return self.current_number


def solve_brute_force():
    """
    Docstring for solve_brute_force().
    """
    lucky_numbers = LuckyNumbers()
    # lucky_numbers.assign_lucky_number(9)
    return lucky_numbers.get_current_number()


# Main ########################################################################

def main():
    result = solve_brute_force()
    print "Solution: Brute Force"
    print "\tThe lucky number is <dramatic pause>", result

    return 0


if __name__ == "__main__":
    main()

#!/usr/bin/env python

"""
PE026: Reciprocal cycles
------------------------

Name: pe026.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-09-03)

Synopsis:
    ``pe026.py``

Examples:
    ``pe026.py``

Description:
    Solution for Project Euler Problem 26
    (https://projecteuler.net/problem=26).

    A unit fraction contains 1 in the numerator. The decimal representation of
    the unit fractions with denominators 2 to 10 are given:

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

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
    be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of :math:`d<1000` for which :math:`1/d` contains the
    longest recurring cycle in its decimal fraction part.
"""


import sys


D_LIMIT = 1000
LUCKY_NUMBER = 7


# Solution: Brute Force #######################################################

class LuckyNumbers():
    """
    Docstring for the class.
    """
    def __init__(self, number):
        """
        Docstring for the initialisation method.
        """
        self.__number = 0
        self.__assign(number)

    def __assign(self, number):
        """
        Docstring for a private method.
        """
        self.__number = number

    def get_lucky(self):
        """
        Docstring for a public method.
        """
        return self.__number


def solve_brute_force(number):
    """
    Docstring for a function.
    """
    lucky_numbers = LuckyNumbers(number)
    return lucky_numbers.get_lucky()


# Main ########################################################################

def main():
    """
    Docstring for the main function.
    """
    result = solve_brute_force(LUCKY_NUMBER)
    print "Solution: Brute Force"
    print "\tDenominator %d leads to the longest recurring cycle." % (result)

    return 0


if __name__ == "__main__":
    main()

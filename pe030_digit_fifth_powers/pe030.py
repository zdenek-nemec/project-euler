#!/usr/bin/env python

"""
PE030: Digit fifth powers
-------------------------

Name: pe030.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-11-01)

Synopsis:
    ``pe030.py``

Examples:
    ``pe030.py``

Description:
    Solution for Project Euler Problem 30
    (https://projecteuler.net/problem=30).

    Surprisingly there are only three numbers that can be written as the sum
    of fourth powers of their digits:

.. math::

    1634 &= 1^4 + 6^4 + 3^4 + 4^4

    8208 &= 8^4 + 2^4 + 0^4 + 8^4

    9474 &= 9^4 + 4^4 + 7^4 + 4^4

..

    As :math:`1 = 1^4` is not a sum it is not included.

    The sum of these numbersis :math:`1637 + 8208 + 9474 = 19316`.

    Find the sum of all the numbers that can be written as the sum of fifth
    powers of their digits.
"""


import sys


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
    print "\tThe lucky number is <dramatic pause> %d!" % (result)

    return 0


if __name__ == "__main__":
    main()

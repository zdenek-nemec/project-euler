#!/usr/bin/env python

"""
PE025: 1000-digit Fibonacci number
----------------------------------

Name: pe025.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-08-20)

Synopsis:
    ``pe025.py``

Examples:
    ``pe025.py``

Description:
    Solution for Project Euler Problem 25
    https://projecteuler.net/problem=25.

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

    What is the index of the first term in the Fibonacci sequence to contain
    1000 digits?
"""


import sys


DIGITS = 1000
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
    print "\tThe index of the first term in the Fibonacci sequence to contain %d digits is %d!" % (DIGITS, result)

    return 0


if __name__ == "__main__":
    main()

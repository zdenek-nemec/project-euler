#!/usr/bin/env python3

"""
PE023: Non-abundant sums
------------------------

Name: pe023.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.2 (2017-11-27)

Synopsis:
    ``pe023.py``

Examples:
    ``pe023.py``

Description:
    Solution for Project Euler Problem 23
    (https://projecteuler.net/problem=23).

    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors
    of 28 would be :math:`1 + 2 + 4 + 7 + 14 = 28`, which means that 28 is a
    perfect number.

    A number :math:`n` is called deficient if the sum of its proper divisors
    is less than :math:`n` and it is called abundant if this sum exceeds
    :math:`n`.

    As 12 is the smallest abundant number, :math:`1 + 2 + 3 + 4 + 6 = 16`, the
    smallest number that can be written as the sum of two abundant numbers is
    24. By mathematical analysis, it can be shown that all integers greater
    than 28123 can be written as the sum of two abundant numbers. However,
    this upper limit cannot be reduced any further by analysis even though it
    is known that the greatest number that cannot be expressed as the sum of
    two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.
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
    print("Solution: Brute Force")
    print("\tSum of all the positive integers which cannot be written as the sum of two abundant number is %d!" % (result))

    return 0


if __name__ == "__main__":
    main()

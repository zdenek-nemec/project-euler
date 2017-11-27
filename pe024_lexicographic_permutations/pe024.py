#!/usr/bin/env python3

"""
PE024: Lexicographic permutations
---------------------------------

Name: pe024.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.2 (2017-11-27)

Synopsis:
    ``pe024.py``

Examples:
    ``pe024.py``

Description:
    Solution for Project Euler Problem 24
    (https://projecteuler.net/problem=24).

    A permutation is an ordered arrangement of objects. For example, 3124 is
    one possible permutation of the digits 1, 2, 3 and 4. If all the
    permutations are listed numerically or alphabetically, we call it
    lexicographic order. The lexocographic permutations of 0, 1 and 2 are:

.. math::

    012 \\ 021 \\ 102 \\ 120 \\ 201 \\ 210

..

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
    4, 5, 6, 7, 8 and 9?
"""


import sys


DIGITS = "0123456789"
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
    print("\tThe millionth lexicographic permutation of the digits %s is %d!" % (DIGITS, result))

    return 0


if __name__ == "__main__":
    main()

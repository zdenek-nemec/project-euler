#!/usr/bin/env python3

"""
PE028: Number spiral diagonals
------------------------------

Name: pe028.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.2 (2017-11-27)

Synopsis:
    ``pe028.py``

Examples:
    ``pe028.py``

Description:
    Solution for Project Euler Problem 28
    (https://projecteuler.net/problem=28).

    Starting with the number 1 and moving to the right in a clockwise
    direction a 5 by 5 spiral is formed as follows:

.. code-block:: none

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

..

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
    formed in the same way?
"""


import sys


LUCKY_NUMBER = 7
SIZE = 5


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
    print("\tThe sum of the number on the diagonals in a %d by %d spiral is %d!" % (SIZE, SIZE, result))

    return 0


if __name__ == "__main__":
    main()

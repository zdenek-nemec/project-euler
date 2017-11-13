#!/usr/bin/env python

"""
PE000: Template
---------------

Name: pe000.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-00-00)

Synopsis:
    ``pe000.py``

Examples:
    ``pe000.py``

Description:
    Solution for Project Euler Problem 0
    (https://projecteuler.net/problem=0).

    This is just a template.
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

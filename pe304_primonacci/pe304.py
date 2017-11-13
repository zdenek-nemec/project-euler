#!/usr/bin/env python

"""
PE304: Primonacci
-----------------

Name: pe304.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-10-18)

Synopsis:
    ``pe304.py``

Examples:
    ``pe304.py``

Description:
    Solution for Project Euler Problem 304
    (https://projecteuler.net/problem=304).

    For any positive integer :math:`n` the function
    :math:`\\text{next_prime}(n)` returns the smallest prime :math:`p` such
    that :math:`p > n`.

    The sequence :math:`a(n)` is defined by:
    :math:`a(1) = \\text{next_prime}(10^{14})` and
    :math:`a(n) = \\text{next_prime}(a(n-1))` for :math:`n>1`.

    The fibonacci sequence :math:`f(n)` is defined by:
    :math:`f(0) = 0, f(1) = 1` and
    :math:`f(n) = f(n-1) + f(n-2)` for :math:`n>1`.

    The sequence :math:`b(n)` is defined as :math:`f(a(n))`.

    Find :math:`\sum b(n)` for :math:`1 \leq n \leq 100000`. Give your answer
    :math:`\\text{mod }1234567891011`.
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

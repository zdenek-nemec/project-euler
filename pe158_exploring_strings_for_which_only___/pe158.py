#!/usr/bin/env python3

"""
PE158: Exploring strings for which only one character comes lexicographically after its neighbour to the left
-------------------------------------------------------------------------------------------------------------

Name: pe158.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.2 (2017-11-27)

Synopsis:
    ``pe158.py``

Examples:
    ``pe158.py``

Description:
    Solution for Project Euler Problem 158
    (https://projecteuler.net/problem=158).

    Taking three different letters from the 26 letters of the alphabet,
    character strings of length three can be formed. Examples are 'abc', hat'
    and 'zyx'. When we study these three examples we see that for 'abc' two
    characters come lexicographically after its neighbour to the left. For
    'hat' there is exactly one character that comes lexicographically after
    its neighbour to the left. For 'zyx' there are zero characters that come
    lexicographically after its neighbour to the left. In all there are 10400
    strings of length 3 for which exactly one character comes
    lexicographically after its neighbout to the left.

    We now consider strings of :math:`n \\leq 26` different characters from
    the alphabet. For every :math:`n`, :math:`\\text{p}(n)` is the number of
    strings of length :math:`n` for which exactly one character comes
    lexicographically after its neighbour to the left.

    What is the maximum value of :math:`\\text{p}(n)`?
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
    print("\tThe maximum value of p(n) is %d!" % (result))

    return 0


if __name__ == "__main__":
    main()

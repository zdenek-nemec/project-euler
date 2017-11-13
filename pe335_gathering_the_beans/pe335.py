#!/usr/bin/env python

"""
PE335: Gathering the beans
--------------------------

Name: pe335.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.1 (2017-11-01)

Synopsis:
    ``pe335.py``

Examples:
    ``pe335.py``

Description:
    Solution for Project Euler Problem 335
    (https://projecteuler.net/problem=335).

    Whenever Peter feels bored, he places some bowls, containing one bean
    each, in a circle. After this, he takes all the beans out of a certain
    bowl and drops them one by one in the bowls going clockwise. He repeats
    this, starting from the bowl he dropped the last bean in, until the
    initial situation appears again. For example with 5 bowls he acts as
    follows:

.. image:: /pe335_gathering_the_beans/p335_mancala.gif
    :align: center

..

    So with 5 bowls it takes Peter 15 moves to return to the initial
    situation.

    Let :math:`M(x)` represent the number of moves required to return to the
    initial situaction, starting with :math:`x` bowls. Thus,
    :math:`M(5) = 15`. It can also be verified that :math:`M(100) = 10920`.

    Find :math:`\sum_{k=0}^{10^{18}} M(2^k + 1)`. Give your answer modulo
    :math:`7^9`.
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

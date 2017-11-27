#!/usr/bin/env python3

"""
PE358: Cyclic numbers
---------------------

Name: pe358.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 0.2 (2017-11-27)

Synopsis:
    ``pe358.py``

Examples:
    ``pe358.py``

Description:
    Solution for Project Euler Problem 358
    (https://projecteuler.net/problem=358).

    A **cyclic number** with :math:`n` digits has a very interesting property:

    When it is multiplied by :math:`1, 2, 3, 4, ... n`, all the products have
    exactly the same digits, in the same order, but rotated in a circular
    fashion!

    The smallest cyclic number is the 6-digid number 142857:

.. math::

    142857 \\times 1 &= 142857

    142857 \\times 2 &= 285714

    142857 \\times 3 &= 428571

    142857 \\times 4 &= 571428

    142857 \\times 5 &= 714285

    142857 \\times 6 &= 857142

..

    The next cyclic number is 0588235294117647 with 16 digits:

.. math::

    0588235294117647 \\times 1 &= 0588235294117647

    0588235294117647 \\times 2 &= 1176470588235294

    0588235294117647 \\times 3 &= 1764705882352941

    ...

    0588235294117647 \\times 16 &= 9411764705882352

..

    Note that for cyclic numbers, leading zeros are important.

    There is only one cyclic number for which, the eleven leftmost digits are
    00000000137 and the five rightmost digits are 56789 (i.e., it has the form
    00000000137...56789 with an unknown number of digits in the middle). Find
    the sum of all its digits.
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
    print("\tThe sum of the digits in the specific cyclic number is %d!" % (result))

    return 0


if __name__ == "__main__":
    main()

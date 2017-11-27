#!/usr/bin/env python3

"""
PE006: Sum square difference
----------------------------

Name: pe006.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe006.py``

Examples:
    ``pe006.py``

Description:
    Solution for Project Euler Problem 6 (https://projecteuler.net/problem=6).

    The sum of the squares of the first ten natural numbers is,

.. math::

    1^2 + 2^2 + ... + 10^2 = 385

..

    The square of the sum of the first ten natural numbers is,

.. math::

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

..

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is :math:`3025 - 385 = 2640`.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
"""


TOP = 100


# Solution: Brute Force #######################################################

def solve_brute_force(top):
    sum_of_squares = 0
    square_of_sums = 0
    for i in range(1, top+1):
        sum_of_squares += i ** 2
        square_of_sums += i
    square_of_sums **= 2
    return (square_of_sums - sum_of_squares)


# Main ########################################################################

def main():
    result = solve_brute_force(TOP)
    print("Solution: Brute Force")
    print("\tDifference between the sum of the squares and the square of the sum of first", TOP, "numbers is", result)
    return 0


if __name__ == "__main__":
    main()

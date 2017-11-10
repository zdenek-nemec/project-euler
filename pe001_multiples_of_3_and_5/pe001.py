#!/usr/bin/env python

"""
PE001: Multiples of 3 and 5
---------------------------

Name: pe001.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.1 (2017-11-10)

Synopsis:
    ``pe001.py``

Examples:
    ``pe001.py``

Description:
    Solution for Project Euler problem 1 (https://projecteuler.net/problem=1).

    If we list all the natural numbers below 10 that are multiples of 3 or 5,
    we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""


LIMIT = 1000
BASES = [3, 5]


# Solution: Modulo ############################################################

class SolutionModulo(object):
    """
    Go through all the numbers under specified limit, check whether they are
    multiples of one of the bases and add them to the sum if yes.
    """
    def __init__(self, limit):
        self._limit = limit

    def sum_multiples(self, bases):
        sum_of_multiples = 0
        for number in xrange(self._limit):
            for base in bases:
                if number % base == 0:
                    sum_of_multiples += number
                    break
        return sum_of_multiples


# Main ########################################################################

def main():
    print SolutionModulo(LIMIT).sum_multiples(BASES)


if __name__ == "__main__":
    main()

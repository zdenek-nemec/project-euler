#!/usr/bin/env python

"""
PE001: Multiples of 3 and 5
---------------------------

Name: pe001.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.3 (2017-11-14)

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


BASES = [3, 5]
LIMIT = 1000


# Solution: Modulo ############################################################

class Multiples(object):
    def __init__(self, bases):
        self._bases = bases

    def sum_multiples(self, limit):
        sum_of_multiples = 0
        for number in xrange(limit):
            for base in self._bases:
                if number % base == 0:
                    sum_of_multiples += number
                    break
        return sum_of_multiples


# Main ########################################################################

def main():
    print Multiples(BASES).sum_multiples(LIMIT)


if __name__ == "__main__":
    main()

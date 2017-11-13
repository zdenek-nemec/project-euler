#!/usr/bin/env python

"""
PE005: Smallest multiple
------------------------

Name: pe005.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.2 (2017-04-22)

Synopsis:
    ``pe005.py``

Examples:
    ``pe005.py``

Description:
    Solution for Project Euler Problem 5 (https://projecteuler.net/problem=5).

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
"""


TOP = 20  # Top digit (divisor)


# Solution: Prime Seed ########################################################

def get_seed(top):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    seed = 1
    for i in primes:
        if (i < top):
            seed *= i
    return seed


def check_div(num, top):
    for i in range(top, 1, -1):
        if ((num % i) != 0):
            return 0
    return 1


def solve_prime_seed(top):
    seed = get_seed(top)
    i = 1
    while True:
        num = i * seed
        if (check_div(num, top)):
            return num
        i += 1
    return 0


# Main ########################################################################

def main():
    result = solve_prime_seed(TOP)
    print "Solution: Prime Seed"
    print "\tThe smallest positive number that is evenly divisible by all of the numbers from 1 to", TOP, "is", result

    return 0


if __name__ == "__main__":
    main()

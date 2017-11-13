#!/usr/bin/env python

"""
PE003: Largest prime factor
---------------------------

Name: pe003.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.2 (2017-04-22)

Synopsis:
    ``pe003.py``

Examples:
    ``pe003.py``

Description:
    Solution for Project Euler Problem 3 (https://projecteuler.net/problem=3).

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
"""


NUM = 600851475143  # Analysed number


# Solution: Brute Force #######################################################

def get_factors(num):
    factors = []
    i = 2
    top = num/2
    while (i <= top):
        if (num % i == 0):
            factors.append(i)
            factors.append(num/i)
        i += 1;
        top = num/i
    factors.sort()
    return factors


def solve_brute_force(num):
    factors = get_factors(num)
    primes = []
    for num in factors:
        tmp = get_factors(num)
        if (tmp == []):
            primes.append(num)
    return primes[len(primes)-1]


# Main ########################################################################

def main():
    result = solve_brute_force(NUM)
    print "Solution: Brute Force"
    print "\tThe largest prime factor of the number", NUM, "is", result

    return 0


if __name__ == "__main__":
    main()

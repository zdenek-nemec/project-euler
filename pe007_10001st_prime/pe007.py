#!/usr/bin/env python

"""
PE007: 10001st prime
--------------------

Name: pe007.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.2 (2017-04-22)

Synopsis:
    ``pe007.py``

Examples:
    ``pe007.py``

Description:
    Solution for Project Euler Problem 7 (https://projecteuler.net/problem=7).

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10001st prime number?
"""


POS = 10001


# Solution: Brute Force #######################################################

def check_prime(num):
    i = 2
    top = num/2
    while (i <= top):
        if ((num % i) == 0):
            return 0
        i += 1
    return 1


def solve_brute_force(pos):
    """
    After 2 go through all odd numbers and check for primes. If the number is
    a prime, put it into a list and scan the specific position. This is
    efective only for primes on positions < 1000.
    """
    primes = [2, 3]
    num = 3
    while True:
        num += 2
        if (check_prime(num)):
            primes.append(num)
            if (len(primes) == pos):
                return num
    return -1


# Solution: Prime Divisor #####################################################

def check_prime_div(num, primes):
    for i in primes:
        if ((num % i) == 0):
            return 0
        if (i > num/2):
            break
    return 1


def solve_prime_divisor(pos):
    """
    Every number that is not a prime should be divisible by a prime. Go
    through all odd numbers after 2 and check their divisibility by primes.
    """
    primes = [2, 3]
    num = 3
    while True:
        num += 2
        if (check_prime_div(num, primes)):
            primes.append(num)
            if (len(primes) == pos):
                return num
    return -1


# Main ########################################################################

def main():
    # result = solve_brute_force(POS)
    # print "Solution: Brute Force"
    # print "\tPrime number on position", POS, "is", result

    result = solve_prime_divisor(POS)
    print "Solution: Prime Divisor"
    print "\tPrime number on position", POS, "is", result
    return 0


if __name__ == "__main__":
    main()

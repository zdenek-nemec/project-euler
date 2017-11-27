#!/usr/bin/env python3

"""
PE010: Summation of primes
--------------------------

Name: pe010.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 3.0 (2017-11-27)

Synopsis:
    ``pe010.py``

Examples:
    ``pe010.py``

Description:
    Solution for Project Euler Problem 10
    (https://projecteuler.net/problem=10).

    The sum of the primes below 10 is :math:`2 + 3 + 5 + 7 = 17`.

    Find the sum of all the primes below two million.
"""


import math


LIMIT = 2000000


# Solution: Prime Divisor #####################################################

def check_prime_div(num, primes):
    # if (((sum(map(int, list(str(num))))) % 3) == 0):  # Optimisation: divisible by 3 = bad idea
    #     return 0
    # if (list(str(num))[-1] == 5):  # Optimisation: divisible by 5 = bad idea
    #     return 0
    cur_limit = math.sqrt(num)  # Optimisation: only 1 prime factor > sqrt(n)
    for i in primes:
        if ((num % i) == 0):
            return 0
        if (i > cur_limit):
            break
    return 1


def solve_prime_divisor(limit):
    """
    Every number that is not a prime should be divisible by a prime. Go
    through all odd numbers after 2 and check their divisibility by primes.
    When checking primes, remember that any number n can have only one
    primefactor greater than square root of n .
    """
    primes = [2, 3]
    num = 3
    while True:
        num += 2
        if (num >= limit):
            break
        if (check_prime_div(num, primes)):
            primes.append(num)
    return sum(primes)


# Main ########################################################################

def main():
    result = solve_prime_divisor(LIMIT)
    print("Solution: Prime Divisor")
    print("\tSum of all prime numbers below", LIMIT, "is", result)
    return 0


if __name__ == "__main__":
    main()

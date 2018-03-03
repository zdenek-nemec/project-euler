#!/usr/bin/env python3

"""
PE-010: Summation of primes
---------------------------

Solution for Project Euler Problem 10 (https://projecteuler.net/problem=10).

The sum of the primes below 10 is :math:`2 + 3 + 5 + 7 = 17`.

Find the sum of all the primes below two million.
"""


import math


LIMIT = 2000000


class Solution(object):
    @staticmethod
    def check_prime_divisor(number, primes):
        current_limit = math.sqrt(number)
        for item in primes:
            if number % item == 0:
                return False
            if item > current_limit:
                break
        return True

    @staticmethod
    def solve(limit):
        """
        Every number that is not a prime should be divisible by a prime. Go
        through all odd numbers after 2 and check their divisibility by primes.
        When checking primes, remember that any number n can have only one
        prime factor greater than square root of n.
        """
        primes = [2, 3]
        number = 3
        while True:
            number += 2
            if number >= limit:
                break
            if Solution().check_prime_divisor(number, primes):
                primes.append(number)
        return sum(primes)


def main():
    print(Solution().solve(LIMIT))


if __name__ == '__main__':
    main()

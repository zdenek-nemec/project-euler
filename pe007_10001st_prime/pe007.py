#!/usr/bin/env python3

"""
PE-007: 10001st prime
---------------------

Solution for Project Euler Problem 7 (https://projecteuler.net/problem=7).

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""


POSITION = 10001


class Solution(object):
    @staticmethod
    def check_prime(number):
        i = 2
        top = number / 2
        while i <= top:
            if number % i == 0:
                return 0
            i += 1
        return 1

    @staticmethod
    def check_prime_divisor(number, primes):
        for i in primes:
            if number % i == 0:
                return 0
            if i > number / 2:
                break
        return 1

    @staticmethod
    def solve(position):
        return Solution().solve_prime_divisor(position)

    @staticmethod
    def solve_brute_force(position):
        """
        After 2 go through all odd numbers and check for primes. If the number
        is a prime, put it into a list and scan the specific position. This is
        effective only for primes on positions < 1000.
        """
        primes = [2, 3]
        number = 3
        while True:
            number += 2
            if Solution().check_prime(number):
                primes.append(number)
                if len(primes) == position:
                    break
        return number

    @staticmethod
    def solve_prime_divisor(position):
        """
        Every number that is not a prime should be divisible by a prime. Go
        through all odd numbers after 2 and check their divisibility by primes.
        """
        primes = [2, 3]
        number = 3
        while True:
            number += 2
            if Solution().check_prime_divisor(number, primes):
                primes.append(number)
                if len(primes) == position:
                    break
        return number


def main():
    print(Solution().solve(POSITION))


if __name__ == '__main__':
    main()

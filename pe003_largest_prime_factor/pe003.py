#!/usr/bin/env python3

"""
PE-003: Largest prime factor
----------------------------

Solution for Project Euler problem 3 (https://projecteuler.net/problem=3).

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


import math


NUMBER = 600851475143


class Factors(object):
    @staticmethod
    def get_factors(number):
        factors = []
        possible_factor = 2
        cap = math.sqrt(number)
        while possible_factor <= cap:
            if number % possible_factor == 0:
                factors.append(possible_factor)
                factors.append(number / possible_factor)
            possible_factor += 1
        factors.sort()
        return factors


class Primes(object):
    @staticmethod
    def is_prime(number):
        prime_flag = False
        if not Factors().get_factors(number):
            prime_flag = True
        return prime_flag


class Solution(object):
    @staticmethod
    def solve(number):
        factors = Factors().get_factors(number)
        primes = []
        for selected_factor in factors:
            if Primes().is_prime(selected_factor):
                primes.append(selected_factor)
        primes.sort()
        return primes[-1]


def main():
    print(Solution().solve(NUMBER))


if __name__ == '__main__':
    main()

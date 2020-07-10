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


class Numbers(object):
    def __init__(self, number):
        self._number = number

    def get_factors(self):
        factors = []
        possible_factor = 2
        cap = math.sqrt(self._number)
        while possible_factor <= cap:
            if self._number % possible_factor == 0:
                factors.append(possible_factor)
                factors.append(self._number // possible_factor)
            possible_factor += 1
        factors.sort()
        return factors

    def is_prime(self):
        if not self.get_factors():
            return True
        return False


class Solution(object):
    def __init__(self, number):
        self._number = number

    def solve(self):
        factors = Numbers(self._number).get_factors()
        primes = []
        for selected_factor in factors:
            if Numbers(selected_factor).is_prime():
                primes.append(selected_factor)
        primes.sort()
        return primes[-1]


def main():
    print(Solution(NUMBER).solve())


if __name__ == '__main__':
    main()

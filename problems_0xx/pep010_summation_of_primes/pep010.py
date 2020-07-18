"""
PEP-010: Summation of primes
----------------------------

Solution for Project Euler problem 10 (https://projecteuler.net/problem=10).

The sum of the primes below 10 is :math:`2 + 3 + 5 + 7 = 17`.

Find the sum of all the primes below two million.
"""

import math

LIMIT = 2000000


class Primes(object):
    def __init__(self):
        self._primes = []

    def add_prime(self, number):
        self._primes.append(number)

    def check_prime(self, number):
        for prime in self._primes:
            if number % prime == 0:
                return 0
            if prime > math.sqrt(number):
                break
        return 1

    def get_all(self):
        return self._primes


class ProjectEulerProblem010(object):
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        number = 1
        primes = Primes()
        primes.add_prime(2)
        while True:
            number += 2
            if number >= self._limit:
                break
            if primes.check_prime(number):
                primes.add_prime(number)
        return sum(primes.get_all())


if __name__ == "__main__":
    print(ProjectEulerProblem010(LIMIT).solve())

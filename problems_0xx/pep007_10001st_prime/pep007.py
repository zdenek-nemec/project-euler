"""
PEP-007: 10001st prime
----------------------

Solution for Project Euler problem 7 (https://projecteuler.net/problem=7).

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10 001st prime number?
"""

import math

POSITION = 10001


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

    def get_length(self):
        return len(self._primes)


class ProjectEulerProblem007(object):
    def __init__(self, position):
        self._position = position

    def solve(self):
        number = 1
        primes = Primes()
        primes.add_prime(2)
        while True:
            number += 2
            if primes.check_prime(number):
                primes.add_prime(number)
                if primes.get_length() == self._position:
                    break
        return number


if __name__ == "__main__":
    print(ProjectEulerProblem007(POSITION).solve())

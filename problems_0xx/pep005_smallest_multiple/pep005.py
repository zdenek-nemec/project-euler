"""
PEP-005: Smallest multiple
--------------------------

Solution for Project Euler problem 5 (https://projecteuler.net/problem=5).

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""

LIMIT = 20


class ProjectEulerProblem005(object):
    def __init__(self, limit):
        self._limit = limit

    def _check_divisibility(self, number):
        for divisor in range(self._limit, 1, -1):
            if number % divisor != 0:
                return False
        return True

    def _get_seed(self):
        prime_list = [2, 3, 5, 7, 11, 13, 17, 19]
        seed = 1
        for prime in prime_list:
            if prime < self._limit:
                seed *= prime
        return seed

    def solve(self):
        seed = self._get_seed()
        number = seed
        while True:
            number += seed
            if self._check_divisibility(number):
                break
        return number


def main():
    print(ProjectEulerProblem005(LIMIT).solve())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
PE-012: Highly divisible triangular number
------------------------------------------

Solution for Project Euler Problem 12 (https://projecteuler.net/problem=12).

The sequence of triangle numbers is generated by adding the natural numbers. So
the 7th triangle number would be :math:`1 + 2 + 3 + 4 + 5 + 6 + 7 = 28`. The
first ten terms would be:

.. math::

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

..

Let us list the factors of the first seven triangle numbers:

.. math::

    1&: 1

    3&: 1, 3

    6&: 1, 2, 3, 6

    10&: 1, 2, 5, 10

    15&: 1, 3, 5, 15

    21&: 1, 3, 7, 21

    28&: 1, 2, 4, 7, 14, 28

..

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred
divisors?
"""


import math


DIVISORS_LIMIT = 500


class Divisors(object):
    def __init__(self):
        self.divisors = {1: [1]}

    def append(self, number):
        if number not in self.divisors:
            divisors = []
            limit = int(math.sqrt(number))
            for i in range(1, limit):
                if number % i == 0:
                    if i not in divisors:
                        divisors.append(i)
                    if number / i not in divisors:
                        divisors.append(number / i)
            self.divisors[number] = divisors

    def get_length(self, number):
        if number not in self.divisors:
            self.append(number)
        return len(self.divisors[number])


class TriangleNumbers(object):
    def __init__(self, numbers=0):
        self.number_list = [1]
        self.last_iteration = 1
        if numbers != 0:
            self.append(numbers - 1)

    def append(self, numbers=1):
        for i in range(0, numbers):
            self.last_iteration += 1
            number = self.number_list[-1] + self.last_iteration
            self.number_list.append(number)

    def get_last(self):
        return self.number_list[-1]

    def get_length(self):
        return len(self.number_list)


class Solution(object):
    def __init__(self, divisors_limit):
        self._divisors_limit = divisors_limit

    def solve(self):
        divisors = Divisors()
        triangle = TriangleNumbers()
        while True:
            if divisors.get_length(triangle.get_last()) > self._divisors_limit:
                break
            triangle.append()
        return triangle.get_last()


def main():
    print(Solution(DIVISORS_LIMIT).solve())


if __name__ == '__main__':
    main()
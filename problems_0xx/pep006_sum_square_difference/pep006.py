"""
PEP-006: Sum square difference
------------------------------

Solution for Project Euler Problem 6 (https://projecteuler.net/problem=6).

The sum of the squares of the first ten natural numbers is,

.. math::

    1^2 + 2^2 + ... + 10^2 = 385

..

The square of the sum of the first ten natural numbers is,

.. math::

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

..

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is :math:`3025 - 385 = 2640`.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

LIMIT = 100


class ProjectEulerProblem006(object):
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        sum_of_squares = 0
        square_of_sums = 0
        for i in range(1, self._limit + 1):
            sum_of_squares += i ** 2
            square_of_sums += i
        square_of_sums **= 2
        return square_of_sums - sum_of_squares


def main():
    print(ProjectEulerProblem006(LIMIT).solve())


if __name__ == "__main__":
    main()

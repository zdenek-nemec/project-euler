#!/usr/bin/env python

"""
PE002: Even Fibonacci numbers
-----------------------------

Name: pe002.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-14)

Synopsis:
    ``pe002.py``

Examples:
    ``pe002.py``

Description:
    Solution for Project Euler Problem 2 (https://projecteuler.net/problem=2).

    Each new term in the Fibonacci sequence is generated by adding the
    previous two terms. By starting with 1 and 2, the first 10 terms will be:

.. math::

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

..

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.
"""


LIMIT = 4000000


# Solution: Sum ###############################################################

class Fibonacci(object):
    def __init__(self, limit):
        self._numbers = self._generate_numbers(limit)

    def _generate_numbers(self, limit):
        numbers = [1, 2]
        while True:
            next_number = self.get_next(numbers)
            if next_number > limit:
                break
            else:
                numbers.append(next_number)
        return numbers

    @staticmethod
    def get_next(numbers):
        return numbers[-2] + numbers[-1]

    def sum_even(self):
        sum_of_even = 0
        for number in self._numbers:
            if number % 2 == 0:
                sum_of_even += number
        return sum_of_even


# Main ########################################################################

def main():
    print Fibonacci(LIMIT).sum_even()


if __name__ == "__main__":
    main()

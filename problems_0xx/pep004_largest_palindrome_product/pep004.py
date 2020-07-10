#!/usr/bin/env python3

"""
PE-004: Largest palindrome product
----------------------------------

Solution for Project Euler problem 4 (https://projecteuler.net/problem=4).

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is :math:`9009 = 91 \\times 99`.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


import math


DIGITS = 3


class Factors(object):
    def __init__(self, number):
        self._number = number

    def _get_factors(self):
        factors = [[1, self._number]]
        possible_factor = 2
        cap = math.sqrt(self._number)
        while possible_factor <= cap:
            if self._number % possible_factor == 0:
                factors.append([possible_factor,
                                self._number // possible_factor])
            possible_factor += 1
        return factors

    def get_factors_with_digits(self, digits):
        factors = self._get_factors()
        selected_factors = []
        for pair in factors:
            length_0 = len(str(pair[0]))
            length_1 = len(str(pair[1]))
            if length_0 == digits and length_1 == digits:
                selected_factors.append(pair)
        return selected_factors


class Palindromes(object):
    def __init__(self, length):
        self._current = int(length * '9')

    def _get_lower(self):
        length = len(str(self._current))
        segment = str(int(str(self._current)[:length // 2]) - 1)
        return int(segment + segment[::-1])

    def get_current(self):
        return self._current

    def set_lower(self):
        self._current = self._get_lower()


class Solution(object):
    def __init__(self, digits):
        self._digits = digits

    def solve(self):
        palindromes = Palindromes(self._digits * 2)
        while True:
            factors = Factors(palindromes.get_current())
            if factors.get_factors_with_digits(self._digits):
                break
            palindromes.set_lower()
        return palindromes.get_current()


def main():
    print(Solution(DIGITS).solve())


if __name__ == '__main__':
    main()

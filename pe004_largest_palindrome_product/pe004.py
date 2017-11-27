#!/usr/bin/env python3

"""
PE004: Largest palindrome product
---------------------------------

Name: pe004.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 3.0 (2017-11-27)

Synopsis:
    ``pe004.py``

Examples:
    ``pe004.py``

Description:
    Solution for Project Euler problem 4 (https://projecteuler.net/problem=4).

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is :math:`9009 = 91 \\times 99`.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""


import math


DIGITS = 3


class Factors(object):
    @staticmethod
    def get_factors(number):
        factors = [[1, number]]
        possible_factor = 2
        cap = math.sqrt(number)
        while possible_factor <= cap:
            if number % possible_factor == 0:
                factors.append([possible_factor, number // possible_factor])
            possible_factor += 1
        return factors

    def get_factors_with_digits(self, number, digits):
        factors = self.get_factors(number)
        selected_factors = []
        for pair in factors:
            length_0 = len(str(pair[0]))
            length_1 = len(str(pair[1]))
            if length_0 == digits and length_1 == digits:
                selected_factors.append(pair)
        return selected_factors


class Palindromes(object):
    def __init__(self, length):
        self._current = int(length * "9")

    def get_current(self):
        return self._current

    def get_lower(self):
        length = len(str(self._current))
        segment = str(int(str(self._current)[:length // 2]) - 1)
        return int(segment + segment[::-1])

    def set_lower(self):
        self._current = self.get_lower()


class SolutionTopToBottom(object):
    @staticmethod
    def solve(digits):
        factors = Factors()
        palindromes = Palindromes(digits * 2)
        while not(
            factors.get_factors_with_digits(palindromes.get_current(), digits)
        ):
            palindromes.set_lower()
        return palindromes.get_current()


def main():
    print(SolutionTopToBottom().solve(DIGITS))


if __name__ == "__main__":
    main()

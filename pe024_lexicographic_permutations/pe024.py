#!/usr/bin/env python3

"""
PE-024: Lexicographic permutations
----------------------------------

Solution for Project Euler Problem 24 (https://projecteuler.net/problem=24).

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

.. math::

    012 \\ 021 \\ 102 \\ 120 \\ 201 \\ 210

..

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
6, 7, 8 and 9?
"""


import itertools


CHARACTERS = '0123456789'
POSITION = 1000000


class Solution(object):
    def __init__(self, characters, position):
        self._characters = characters
        self._position = position

    def solve(self):
        permutation_list = list(
            itertools.permutations(self._characters, len(self._characters)))
        permutation_tuple = permutation_list[self._position - 1]
        permutation = ''
        for character in permutation_tuple:
            permutation += character
        return permutation


def main():
    print(Solution(CHARACTERS, POSITION).solve())


if __name__ == '__main__':
    main()

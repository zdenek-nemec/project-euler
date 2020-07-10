#!/usr/bin/env python3

"""
PE-158: Exploring strings for which only one character comes lexicographically \
after its neighbour to the left
-------------------------------------------------------------------------------\
-------------------------------

Solution for Project Euler Problem 158 (https://projecteuler.net/problem=158).

Taking three different letters from the 26 letters of the alphabet, character
strings of length three can be formed. Examples are 'abc', hat' and 'zyx'. When
we study these three examples we see that for 'abc' two characters come
lexicographically after its neighbour to the left. For 'hat' there is exactly
one character that comes lexicographically after its neighbour to the left. For
'zyx' there are zero characters that come lexicographically after its neighbour
to the left. In all there are 10400 strings of length 3 for which exactly one
character comes lexicographically after its neighbour to the left.

We now consider strings of :math:`n \\leq 26` different characters from the
alphabet. For every :math:`n`, :math:`\\text{p}(n)` is the number of strings of
length :math:`n` for which exactly one character comes lexicographically after
its neighbour to the left.

What is the maximum value of :math:`\\text{p}(n)`?

.. warning:: Open
"""


class Solution(object):
    @staticmethod
    def solve():
        return 0


def main():
    print(Solution().solve())


if __name__ == '__main__':
    main()

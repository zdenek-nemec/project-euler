#!/usr/bin/env python3

"""
PE-014: Longest Collatz sequence
--------------------------------

Solution for Project Euler Problem 14 (https://projecteuler.net/problem=14).

The following iterative sequence is defined for the set of positive integers:

:math:`n \\rightarrow n/2` (:math:`n` is even)

:math:`n \\rightarrow 3n + 1` (:math:`n` is odd)

Using the rule above and starting with 13, we generate the following sequence:

.. math::

    13 \\rightarrow
    40 \\rightarrow
    20 \\rightarrow
    10 \\rightarrow
    5 \\rightarrow
    16 \\rightarrow
    8 \\rightarrow
    4 \\rightarrow
    2 \\rightarrow
    1

..

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

**NOTE**: Once the chain starts the terms are allowed to go above one million.
"""


LIMIT = 1000000


class Solution(object):
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        """
        Explore the range from bottom to top. For even numbers use references to
        already existing dictionary. Calculate Collatz sequence only for odd
        numbers and their followers.
        """
        collatz = {}
        for i in range(1, self._limit):
            if i % 2 == 0:
                collatz[i] = collatz[i/2] + 1
            else:
                sequence = [i]
                last = i
                extra = 0
                while last != 1:
                    if last in collatz:
                        extra = collatz[last] - 1
                        break
                    elif last % 2 == 0:
                        last = last / 2
                    else:
                        last = last * 3 + 1
                    sequence.append(last)
                collatz[i] = len(sequence) + extra
        sorted_collatz = sorted(collatz.items(), key=lambda x: x[1])
        number, chain_length = sorted_collatz[-1]
        return number


def main():
    print(Solution(LIMIT).solve())


if __name__ == '__main__':
    main()

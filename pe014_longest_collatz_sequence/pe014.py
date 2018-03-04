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


import operator


LIMIT = 1000000


class CollatzSequence(object):
    def __init__(self, start=1):
        self._start = start
        self._sequence = [start]
        while self._get_last() != 1:
            self._sequence.append(self._get_next())

    def _get_last(self):
        return self._sequence[-1]

    def _get_next(self):
        if self._get_last() % 2 == 0:
            return self._get_last() / 2
        else:
            return self._get_last() * 3 + 1

    def get_len(self):
        return len(self._sequence)

    def get_sequence(self):
        return self._sequence


class Solution(object):
    @staticmethod
    def solve(limit):
        return Solution().solve_dictionary(limit)

    @staticmethod
    def solve_brute_force(limit):
        """
        Generate all Collatz sequences in a given range, check their length and
        return the longest one.
        """
        max_start = 1
        max_length = 1
        for i in range(1, limit):
            collatz = CollatzSequence(i)
            if collatz.get_len() > max_length:
                max_start = i
                max_length = collatz.get_len()
        return max_start

    @staticmethod
    def solve_brute_force_optimized(limit):
        """
        Gnerate all Collatz sequences in a given range using only sequences and
        dictionaries. Optimise in order to avoid calculating sequences multiple
        times.
        """
        collatz = {}
        for i in range(1, limit):
            sequence = [i]
            last = i
            extra_length = 0
            while last != 1:
                if last in collatz:
                    extra_length = collatz[last] - 1
                    break
                elif last % 2 == 0:
                    last = last / 2
                else:
                    last = last * 3 + 1
                sequence.append(last)
            collatz[i] = len(sequence) + extra_length
        sorted_collatz = sorted(collatz.items(), key=operator.itemgetter(1))
        return sorted_collatz[-1][0]

    @staticmethod
    def solve_dictionary(limit):
        """
        Explore the range from bottom to top. For even numbers use references to
        already existing dictionary. Calculate Collatz sequence only for odd
        numbers and their followers.
        """
        collatz = {}
        for i in range(1, limit):
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
        sorted_collatz = sorted(collatz.items(), key=operator.itemgetter(1))
        return sorted_collatz[-1][0]


def main():
    print(Solution().solve(LIMIT))


if __name__ == '__main__':
    main()

#!/usr/bin/env python

"""
PE014: Longest Collatz sequence
-------------------------------

Name: pe014.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.1 (2017-05-03)

Synopsis:
    ``pe014.py``

Examples:
    ``pe014.py``

Description:
    Solution for Project Euler Problem 14
    (https://projecteuler.net/problem=14).

    The following iterative sequence is defined for the set of positive
    integers:

    :math:`n \\rightarrow n/2` (:math:`n` is even)

    :math:`n \\rightarrow 3n + 1` (:math:`n` is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

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

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

.. note::
    Once the chain starts the terms are allowed to go above one million.
"""


import operator


LIMIT = 1000000


# Solution: Brute Force #######################################################

class CollatzSequence():
    """
    Collatz sequence for given start number.
    """
    def __init__(self, start = 1):
        self.__start = start
        self.__sequence = [start]
        while (self.__get_last() != 1):
            self.__sequence.append(self.__get_next())

    def __get_last(self):
        """
        Retrieve last term of the seqence.
        """
        return self.__sequence[len(self.__sequence) - 1]

    def __get_next(self):
        """
        Calculate next term of the sequence.
        """
        if (self.__get_last() % 2 == 0):
            return (self.__get_last() / 2)
        else:
            return (self.__get_last() * 3 + 1)

    def get_len(self):
        """
        Retrieve length of the sequence.
        """
        return len(self.__sequence)

    def get_sequence(self):
        """
        Retrieve the sequence.
        """
        return self.__sequence


def solve_brute_force(limit):
    """
    Generate all Collatz sequences in given range using OOP (class), check
    their length and save the longest.
    """
    max_start = 1
    max_len = 1
    for i in range(1, limit):
        collatz = CollatzSequence(i)
        if (collatz.get_len() > max_len):
            max_start = i
            max_len = collatz.get_len()
    return max_start


# Solution: Brute Force Optimized #############################################

def solve_brute_force_optimized(limit):
    """
    Gnerate all Collatz sequences in given range using only sequences and
    dictionaries. Optimise in order to avoid calculating sequences multiple
    times.
    """
    collatz = {1 : 1}
    for i in range(1, limit):
        sequence = [i]
        last = i
        extra_len = 0
        # mid = {}
        while (last != 1):
            if (last in collatz):
                extra_len = collatz[last] - 1
                break
            elif (last % 2 == 0):
                last = last / 2
            else:
                last = last * 3 + 1
                # if (not(last in collatz)):
                #     mid[last] = -len(sequence)
            sequence.append(last)
        collatz[i] = len(sequence) + extra_len
        # for d in mid:
        #     collatz[d] = len(sequence) + mid[d]
    sorted_collatz = sorted(collatz.items(), key = operator.itemgetter(1))

    return (sorted_collatz[len(sorted_collatz) - 1][0])


# Solution: Dictionary ########################################################

def solve_dictionary(limit):
    """
    Explore the range from bottom to top. For even numbers use references to
    already existing dictionary. Calculate Collatz sequence only for odd
    numbers and their followers.
    """
    collatz = {}
    for i in range(1, limit):
        if (i % 2 == 0):
            collatz[i] = collatz[i/2] + 1
        else:
            sequence = [i]
            last = i
            extra = 0
            while (last != 1):
                if (last in collatz):
                    extra = collatz[last] - 1
                    break
                elif (last % 2 == 0):
                    last = last / 2
                else:
                    last = last * 3 + 1
                sequence.append(last)
            collatz[i] = len(sequence) + extra
    sorted_collatz = sorted(collatz.items(), key = operator.itemgetter(1))

    return (sorted_collatz[len(sorted_collatz) - 1][0])


# Main ########################################################################

def main():
    # result = solve_brute_force(LIMIT)
    # print "Solution: Brute Force"
    # print "\tStarting number", result, ", of those under", LIMIT, ", produces the longest chain."

    # result = solve_brute_force_optimized(LIMIT)
    # print "Solution: Brute Force Optimized"
    # print "\tStarting number", result, ", of those under", LIMIT, ", produces the longest chain."

    result = solve_dictionary(LIMIT)
    print "Solution: Dictionary"
    print "\tStarting number", result, ", of those under", LIMIT, ", produces the longest chain."

    return 0


if __name__ == "__main__":
    main()

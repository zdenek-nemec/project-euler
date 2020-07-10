#!/usr/bin/env python3

"""
PE-023: Non-abundant sums
-------------------------

Solution for Project Euler Problem 23 (https://projecteuler.net/problem=23).

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be
:math:`1 + 2 + 4 + 7 + 14 = 28`, which means that 28 is a perfect number.

A number :math:`n` is called deficient if the sum of its proper divisors is less
than :math:`n` and it is called abundant if this sum exceeds :math:`n`.

As 12 is the smallest abundant number, :math:`1 + 2 + 3 + 4 + 6 = 16`, the
smallest number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

.. warning:: Open
"""


import math
import time


# LIMIT = 28123
LIMIT = 3000


class Divisors(object):
    @staticmethod
    def get_divisors(number):
        divisors = [1]
        for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                divisors.append(divisor)
                if number // divisor not in divisors:
                    divisors.append(number // divisor)
        return sorted(divisors)


class SolutionA(object):
    """
    Make a list of abundant numbers. Go through all integers below the limit,
    subtract abundant number and check whether the result is abundant or not.
    If non-abundant, add to the total.

    .. note:: Too slow
    """
    @staticmethod
    def solve(limit):
        abundant_list = []
        for number in range(1, limit + 1):
            divisors = Divisors().get_divisors(number)
            if sum(divisors) > number:
                abundant_list.append(number)
        total_sum = 0
        for number in range(1, limit + 1):
            non_abundant_sum = True
            for abundant in abundant_list:
                if number - abundant in abundant_list:
                    non_abundant_sum = False
                    break
                if 2 * abundant > number:
                    break
            if non_abundant_sum:
                total_sum += number
        return total_sum


class SolutionB(object):
    """
    Make a list of abundant numbers. Calculate all abundant sums. Go through all
    integers below the limit and add all non-abundant to the total.

    .. note:: Too slow
    """
    @staticmethod
    def solve(limit):
        abundant_list = []
        for number in range(1, limit + 1):
            divisors = Divisors().get_divisors(number)
            if sum(divisors) > number:
                abundant_list.append(number)
        abundant_sum_list = []
        for index_a in range(0, len(abundant_list)):
            for index_b in range(index_a, len(abundant_list)):
                abundant_sum = abundant_list[index_a] + abundant_list[index_b]
                if abundant_sum > limit:
                    break
                if abundant_sum not in abundant_sum_list:
                    abundant_sum_list.append(abundant_sum)
        total_sum = 0
        for number in range(1, limit + 1):
            if number not in abundant_sum_list:
                total_sum += number
        return total_sum


class Solution(object):
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        start_timestamp = time.time()
        print('A:', SolutionA().solve(self._limit))
        end_timestamp = time.time()
        print('%.2f' % (end_timestamp - start_timestamp))

        start_timestamp = time.time()
        print('B:', SolutionB().solve(self._limit))
        end_timestamp = time.time()
        print('%.2f' % (end_timestamp - start_timestamp))

        return 0


def main():
    print(Solution(LIMIT).solve())


if __name__ == '__main__':
    main()

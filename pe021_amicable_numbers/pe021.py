#!/usr/bin/env python3

"""
PE021: Amicable numbers
-----------------------

Name: pe021.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe021.py``

Examples:
    ``pe021.py``

Description:
    Solution for Project Euler Problem 21
    (https://projecteuler.net/problem=21).

    Let :math:`d(n)` be defined as the sum of proper divisors of :math:`n`
    (numbers less than :math:`n` which divide evenly into :math:`n`). If
    :math:`d(a) = b` and :math:`d(b) = a`, where :math:`a \\neq b`, then
    :math:`a` and :math:`b` are an amicable pair and each of :math:`a` and
    :math:`b` are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
    44, 55 and 110; therefore :math:`d(220) = 284`. The proper divisors of 284
    are 1, 2, 4, 71 and 142; so :math:`d(284) = 220`.

    Evaluate the sum of all the amicable numbers under 10000.
"""


import math


LIMIT = 10000


# Solution: Brute Force #######################################################

def get_divisors(number):
    """
    Retrieve all proper divisors of the number.
    """
    divs = []
    for i in range(number - 1, 0, -1):
        if (number % i == 0):
            divs.append(i)
    return divs


def solve_brute_force(limit):
    """
    Calculate list of sums for all the numbers under the limit, then go
    through the list and search for amicable numbers, return their sum.
    """
    sums = [0]
    for i in range(1, limit + 1):
        sums.append(sum(get_divisors(i)))

    amicable = []
    for i in range(1, limit + 1):
        if (sums[i] > limit):
            continue
        if (sums[i] == i):
            continue
        if (sums[sums[i]] == i):
            amicable.append(i)

    return sum(amicable)


# Solution: Optimalized #######################################################

class Divisors():
    """Proper divisors for numbers."""
    def __init__(self, number = 1):
        """
        Setup Divisors object and load first number.
        """
        self.__divisors = {}
        self.__evaluate(number)

    def __evaluate(self, number):
        """
        Calculate list of proper divisors for a number.
        """
        divs = [1]
        for i in range(1, int(math.sqrt(number))):
            if (i in divs):
                continue
            elif (number % i == 0):
                divs.append(i)
                divs.append(number / i)
        self.__divisors[number] = divs

    def get(self, number):
        """
        Retrieve list of proper divisors for a number.
        """
        if not(number in self.__divisors):
            self.__evaluate(number)
        return self.__divisors[number]

    def print_divisors(self):
        """
        Print Divisors structure currently in memory.
        """
        print(self.__divisors)


def solve_optimized(limit):
    """
    Go through all the numbers under the limit, calculate sums in pairs and
    check whether the numbers are amicable pair or not. Return the sum of all
    amicable numbers under the given limit.
    """
    divs = Divisors()
    sums = {}
    amicable = []
    for i in range(1, limit + 1):
        if (i in amicable):
            continue
        if not(i in sums):
            sums[i] = sum(divs.get(i))
        if ((sums[i] > limit) or (sums[i] == i)):
            continue
        if not(sums[i] in sums):
            sums[sums[i]] = sum(divs.get(sums[i]))
        if (sums[sums[i]] == i):
            amicable.append(i)
            amicable.append(sums[i])

    return sum(amicable)


# Main ########################################################################

def main():
    # result = solve_brute_force(LIMIT)
    # print "Solution: Brute Force"
    # print "\tThe sum of all the amicable numbers under %d is %d." % (LIMIT, result)

    result = solve_optimized(LIMIT)
    print("Solution: Optimized")
    print("\tThe sum of all the amicable numbers under %d is %d." % (LIMIT, result))

    return 0


if __name__ == "__main__":
    main()

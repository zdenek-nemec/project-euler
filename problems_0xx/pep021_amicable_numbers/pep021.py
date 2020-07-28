"""
PEP-021: Amicable numbers
-------------------------

Solution for Project Euler problem 21 (https://projecteuler.net/problem=21).

Let :math:`d(n)` be defined as the sum of proper divisors of :math:`n` (numbers
less than :math:`n` which divide evenly into :math:`n`). If :math:`d(a) = b` and
:math:`d(b) = a`, where :math:`a \\neq b`, then :math:`a` and :math:`b` are an
amicable pair and each of :math:`a` and :math:`b` are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore :math:`d(220) = 284`. The proper divisors of 284 are 1, 2, 4,
71 and 142; so :math:`d(284) = 220`.

Evaluate the sum of all the amicable numbers under 10000.
"""

import math

LIMIT = 10000


class Divisors(object):
    """
    Proper divisors for numbers.
    """

    def __init__(self, number=1):
        """
        Setup Divisors object and load first number.
        """
        self._divisors = {}
        self._evaluate(number)

    def _evaluate(self, number):
        """
        Calculate list of proper divisors for a number.
        """
        divisors = [1]
        for i in range(1, int(math.sqrt(number))):
            if i in divisors:
                continue
            elif number % i == 0:
                divisors.append(i)
                divisors.append(number // i)
        self._divisors[number] = divisors

    def get(self, number):
        """
        Retrieve list of proper divisors for a number.
        """
        if number not in self._divisors:
            self._evaluate(number)
        return self._divisors[number]

    def print_divisors(self):
        """
        Print Divisors structure currently in memory.
        """
        print(self._divisors)


class ProjectEulerProblem021(object):
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        """
        Go through all the numbers under the limit, calculate sums in pairs and
        check whether the numbers are amicable pair or not. Return the sum of
        all amicable numbers under the given limit.
        """
        divisors = Divisors()
        sums = {}
        amicable = []
        for i in range(1, self._limit + 1):
            if i in amicable:
                continue
            if i not in sums:
                sums[i] = sum(divisors.get(i))
            if sums[i] > self._limit or sums[i] == i:
                continue
            if sums[i] not in sums:
                sums[sums[i]] = sum(divisors.get(sums[i]))
            if sums[sums[i]] == i:
                amicable.append(i)
                amicable.append(sums[i])
        return sum(amicable)


if __name__ == "__main__":
    print(ProjectEulerProblem021(LIMIT).solve())

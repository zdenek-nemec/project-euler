"""
PEP-001: Multiples of 3 and 5
-----------------------------

Solution for Project Euler problem 1 (https://projecteuler.net/problem=1).

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

MULTIPLIERS = [3, 5]
LIMIT = 1000


class ProjectEulerProblem001(object):
    def __init__(self, multipliers, limit):
        self._multipliers = multipliers
        self._limit = limit

    def _is_multiple(self, number):
        for multiplier in self._multipliers:
            if number % multiplier == 0:
                return True
        return False

    def solve(self):
        sum_of_multiples = 0
        for number in range(self._limit):
            if self._is_multiple(number):
                sum_of_multiples += number
        return sum_of_multiples


if __name__ == "__main__":
    print(ProjectEulerProblem001(MULTIPLIERS, LIMIT).solve())

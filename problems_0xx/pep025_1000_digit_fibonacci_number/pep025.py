"""
PEP-025: 1000-digit Fibonacci number
------------------------------------

Solution for Project Euler problem 25 (https://projecteuler.net/problem=25).

The Fibonacci sequence is defined by the recurrence relation:

:math:`F_{n} = F_{n-1} + F_{n-2}`, where :math:`F_1 = 1` and
:math:`F_2 = 1`.

Hence the first 12 terms will be:

.. math::

    F_{1} &= 1

    F_{2} &= 1

    F_{3} &= 2

    F_{4} &= 3

    F_{5} &= 5

    F_{6} &= 8

    F_{7} &= 13

    F_{8} &= 21

    F_{9} &= 34

    F_{10} &= 55

    F_{11} &= 89

    F_{12} &= 144

..

The 12th term, :math:`F_12`, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""

DIGITS = 1000
START = [1, 1]


class Fibonacci(object):
    def __init__(self, start):
        self._series = start

    def append_next(self):
        next_number = self._series[-2] + self._series[-1]
        self._series.append(next_number)

    def get_all(self):
        return self._series

    def get_last(self):
        return self._series[-1]

    def get_length(self):
        return len(self._series)


class ProjectEulerProblem025(object):
    def __init__(self, digits, start):
        self._digits = digits
        self._start = start

    def solve(self):
        fibonacci = Fibonacci(self._start)
        while len(str(fibonacci.get_last())) < self._digits:
            fibonacci.append_next()
        return fibonacci.get_length()


if __name__ == "__main__":
    print(ProjectEulerProblem025(DIGITS, START).solve())

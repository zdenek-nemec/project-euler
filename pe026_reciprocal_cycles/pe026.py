#!/usr/bin/env python3

"""
PE-026: Reciprocal cycles
-------------------------

Solution for Project Euler Problem 26 (https://projecteuler.net/problem=26).

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

.. math::

    1/2 &= 0.5

    1/3 &= 0.(3)

    1/4 &= 0.25

    1/5 &= 0.2

    1/6 &= 0.1(6)

    1/7 &= 0.(142857)

    1/8 &= 0.125

    1/9 &= 0.(1)

    1/10 &= 0.1

..

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of :math:`d<1000` for which :math:`1/d` contains the longest
recurring cycle in its decimal fraction part.

.. warning:: Open
"""


LIMIT = 1000


class Dividend(object):
    def __init__(self, number, denominator):
        self._number = number
        self._denominator = denominator
        self._dividend = []
        self._remainder_history = []
        self._remainder = number
        self._cycle = []

    def append_partial(self):
        if self._denominator > self._remainder:
            self._dividend.append(0)
            self._remainder_history.append(self._remainder)
            self._remainder *= 10
        else:
            dividend = self._remainder // self._denominator
            self._dividend.append(dividend)
            self._remainder %= self._denominator
            self._remainder_history.append(self._remainder)
            self._remainder *= 10

    def calculate(self):
        while True:
            self.append_partial()
            if self._remainder == 0:
                break
            if self.check_cycle():
                break

    def check_cycle(self):
        if self._dividend[-1] == 0:
            return False
        for i in range(1, len(self._dividend)):
            if (self._dividend[-i:] == self._dividend[-i*2:-i] and self._remainder_history[-i:] == self._remainder_history[-i * 2:-i]):
                self._cycle = self._dividend[-i:]
                return True
        return False

    def get_cycle(self):
        return self._cycle

    def get_dividend(self):
        return self._dividend


class Solution(object):
    """
    .. note:: Too slow, needs cleaning
    """
    def __init__(self, limit):
        self._limit = limit

    def solve(self):
        longest_cycle_denominator = 0
        longest_cycle_length = 0
        for denominator in range(2, self._limit):
            dividend = Dividend(1, denominator)
            dividend.calculate()
            cycle_length = len(dividend.get_cycle())
            # if cycle_length > 0:
            #     print(denominator, dividend.get_dividend(), dividend.get_cycle())
            if cycle_length > longest_cycle_length:
                longest_cycle_length = cycle_length
                longest_cycle_denominator = denominator
                print(denominator, dividend.get_dividend(),
                      len(dividend.get_cycle()))
        return longest_cycle_denominator


if __name__ == '__main__':
    print(Solution(LIMIT).solve())

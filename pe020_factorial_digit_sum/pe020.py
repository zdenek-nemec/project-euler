#!/usr/bin/env python3

"""
PE-020: Factorial digit sum
---------------------------

Solution for Project Euler Problem 20 (https://projecteuler.net/problem=20).

:math:`n!` means
:math:`n \\times (n - 1) \\times ... \\times 3 \\times 2 \\times 1`

For example,
:math:`10! = 10 \\times 9 \\times ... \\times 3 \\times 2 \\times 1 =
3628800`, and the sum of the digits in the number :math:`10!` is
:math:`3 + 6 + 2 + 8 + 8 + 0 + 0 = 27`.

Find the sum of the digits in the number :math:`100!`.
"""


NUMBER = 100


class Solution(object):
    @staticmethod
    def solve(number):
        """
        Using a cycle calculate the factorial and cycle through the string of
        that number afterwards and make a sum.
        """
        factorial = 1
        for i in range(1, number + 1):
            factorial *= i
        factorial_sum = 0
        for c in str(factorial):
            factorial_sum += int(c)
        return factorial_sum


def main():
    print(Solution().solve(NUMBER))


if __name__ == '__main__':
    main()

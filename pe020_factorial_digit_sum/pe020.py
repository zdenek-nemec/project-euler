#!/usr/bin/env python

"""
PE020: Factorial digit sum
--------------------------

Name: pe020.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.0 (2017-06-12)

Synopsis:
    ``pe020.py``

Examples:
    ``pe020.py``

Description:
    Solution for Project Euler Problem 20
    (https://projecteuler.net/problem=20).

    :math:`n!` means
    :math:`n \\times (n - 1) \\times ... \\times 3 \\times 2 \\times 1`

    For example,
    :math:`10! = 10 \\times 9 \\times ... \\times 3 \\times 2 \\times 1 =
    3628800`, and the sum of the digits in the number :math:`10!` is
    :math:`3 + 6 + 2 + 8 + 8 + 0 + 0 = 27`.

    Find the sum of the digits in the number :math:`100!`.
"""


NUMBER = 100


# Solution: Brute Force #######################################################

def solve_brute_force(number):
    """
    Using a cycle calculate the factorial and cycle through the string of that
    number afterwards and make a sum.
    """
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    f_sum = 0
    for c in str(factorial):
        f_sum += int(c)
    return f_sum


# Main ########################################################################

def main():
    result = solve_brute_force(NUMBER)
    print "Solution: Brute Force"
    print "\tThe sum of the digits in the %d! is %d." % (NUMBER, result)

    return 0


if __name__ == "__main__":
    main()

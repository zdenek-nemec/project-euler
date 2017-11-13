#!/usr/bin/env python

"""
PE016: Power digit sum
----------------------

Name: pe016.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.0 (2017-05-21)

Synopsis:
    ``pe016.py``

Examples:
    ``pe016.py``

Description:
    Solution for Project Euler Problem 16
    (https://projecteuler.net/problem=16).

    :math:`2^{15} = 32768` and the sum of its digits is
    :math:`3 + 2 + 7 + 6 + 8 = 26`.

    What is the sum of the digits of the number :math:`2^{1000}`?
"""


POWER = 1000


# Solution: Brute Force #######################################################

def solve_brute_force(power):
    """
    Calculate the power number, convert it to text and make a sum of
    all the digits.
    """
    number = pow(2, power)
    number_str = str(number)
    power_sum = 0
    for c in number_str:
        power_sum += int(c)
    return power_sum


# Main ########################################################################

def main():
    result = solve_brute_force(POWER)
    print "Solution: Brute Force"
    print "\tThe sum of the digits of the number 2 ^", POWER, "is", result

    return 0


if __name__ == "__main__":
    main()

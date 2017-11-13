#!/usr/bin/env python

"""
PE004:  Largest palindrome product
----------------------------------

Name: pe004.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 1.2 (2017-04-22)

Synopsis:
    ``pe004.py``

Examples:
    ``pe004.py``

Description:
    Solution for Project Euler Problem 4 (https://projecteuler.net/problem=4).

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is :math:`9009 = 91 \\times 99`.

    Find the largest palindrome made from the product of two 3-digit numbers.

.. warning::
    **Error**: Palindromes with odd number of digits are omitted!
"""


DIGITS = 3  # Digits in both factors of palindromic number


# Solution: Brute Force #######################################################

def get_factors(num, digits):
    factors = []
    i = 2
    top = num/2
    while (i <= top):
        if (num % i == 0):
            if ((len(str(i)) == digits) and (len(str(top)) == digits)):
                factors.append(i)
                factors.append(num/i)
                break
        i += 1;
        top = num/i
    return factors


def get_lower_pn(last):
    last_str = str(last)
    assert ((len(last_str) % 2) == 0), "Number of digits is expected to be even."
    last_left = int(last_str[:len(last_str)/2])
    new_left = last_left-1
    new_str = str(new_left) + str(new_left)[::-1]  # Extended slice (reverse string)
    new = int(new_str)
    return new


def solve_brute_force(digits):
    num = ((10 ** digits) ** 2) - 1
    while True:
        factors = get_factors(num, digits)
        if (factors != []):
            return num
            break
        if (num == 0):
            break
        num = get_lower_pn(num)

    return 0


# Main ########################################################################

def main():
    result = solve_brute_force(DIGITS)
    print "Solution: Brute Force"
    print "\tThe largest palindrome made from the product of two", DIGITS, "digit numbers is", result

    return 0


if __name__ == "__main__":
    main()

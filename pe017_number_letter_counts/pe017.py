#!/usr/bin/env python3

"""
PE017: Number letter counts
---------------------------

Name: pe017.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe017.py``

Examples:
    ``pe017.py``

Description:
    Solution for Project Euler Problem 17
    (https://projecteuler.net/problem=17).

    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are :math:`3 + 3 + 5 + 4 + 4 = 19` letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

.. note::
    Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.
"""


TOP = 1000


# Solution: Brute Force #######################################################

def count_letters(phrase):
    """
    Count only letters 'a'..'z' in a string.
    """
    letter_count = 0
    for c in phrase:
        if ((c >= 'a') and (c <= 'z')):
            letter_count += 1
    return letter_count


def solve_brute_force(top):
    """
    Generate names for all the numbers, count the letters and make a sum.
    """
    numbers = {
        1 : "one",
        2 : "two",
        3 : "three",
        4 : "four",
        5 : "five",
        6 : "six",
        7 : "seven",
        8 : "eight",
        9 : "nine",
        10 : "ten",
        11 : "eleven",
        12 : "twelve",
        13 : "thirteen",
        14 : "fourteen",
        15 : "fifteem",
        16 : "sixteen",
        17 : "seventeen",
        18 : "eighteen",
        19 : "nineteen",
        20 : "twenty",
        30 : "thirty",
        40 : "forty",
        50 : "fifty",
        60 : "sixty",
        70 : "seventy",
        80 : "eighty",
        90 : "ninety",
        100 : "hundred",
        1000 : "thousand"
    }

    total_letters = 0
    for i in range(1, top + 1):
        num = i
        name = ""
        name_len = 0
        if (num >= 1000):
            name += numbers[num // 1000] + " " + numbers[1000]
            num %= 1000
            if ((num < 100) and (num != 0)):
                name += " and "
            elif (num != 0):
                name += " "
        if (num >= 100):
            name += numbers[num // 100] + " " + numbers[100]
            num %= 100
            if (num != 0):
                name += " and "
        if ((num > 20) and (num % 10 != 0)):
            name += numbers[num // 10 * 10] + "-" + numbers[num % 10]
        elif (num != 0):
            name += numbers[num]
        # print i, ":", name, ":", count_letters(name)
        total_letters += count_letters(name)

    return total_letters


# Main ########################################################################

def main():
    result = solve_brute_force(TOP)
    print("Solution: Brute Force")
    print("\tList of all the numbers in interval 1 to", TOP, "uses", result, "letters.")

    return 0


if __name__ == "__main__":
    main()

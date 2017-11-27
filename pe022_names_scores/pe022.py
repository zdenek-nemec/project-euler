#!/usr/bin/env python3

"""
PE022: Names scores
-------------------

Name: pe022.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe022.py``

Examples:
    ``pe022.py``

Description:
    Solution for Project Euler Problem 22
    (https://projecteuler.net/problem=22).

    Using :download:`names.txt</pe022_names_scores/p022_names.txt>` (right
    click and 'Save Link/Target As...'), a 46K text file containing over
    five-thousand first names, begin by sorting it into alphabetical order.
    Then working out the alhapetical value for each name, multiply this value
    by its alphabetical position in the list to obtain a name score.

    For example, when the list is sorted into aplhabetical order, COLIN, which
    is worth :math:`3 + 15 + 12 + 9 + 14 = 53`, is the 938th name in the list.
    So COLIN would obtain a score of :math:`938 \\times 53 = 49714`.

    What is the total of all the name scores in the file?
"""


INPUT_FILE = "p022_names.txt"


# Solution: Sorted List #######################################################

def solve_sorted_list(input_file):
    """
    Load the names into a list with calculated score, sort the list and
    evaluate.
    """
    names = []
    with open(input_file, "r") as f:
        name = ""
        score = 0
        while (1):
            c = f.read(1)
            if (c == '\"'):
                continue
            elif ((c == ',') or (c == '')):
                names.append((name, score))
                name = ""
                score = 0
            else:
                name += c
                score += ord(c) - ord('A') + 1
            if (c == ''):
                break

    total = 0
    i = 0
    for entry in sorted(names):
        i += 1
        total += i * entry[1]

    return total


# Main ########################################################################

def main():
    result = solve_sorted_list(INPUT_FILE)
    print("Solution: Sorted List")
    print("\tTotal of all the name scores in the file is %d." % (result))

    return 0


if __name__ == "__main__":
    main()

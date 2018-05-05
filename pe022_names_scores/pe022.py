#!/usr/bin/env python3

"""
PE-022: Names scores
--------------------

Solution for Project Euler Problem 22 (https://projecteuler.net/problem=22).

Using :download:`names.txt</pe022_names_scores/p022_names.txt>` (right click and
'Save Link/Target As...'), a 46K text file containing over five-thousand first
names, begin by sorting it into alphabetical order. Then working out the
alphabetical value for each name, multiply this value by its alphabetical
position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth :math:`3 + 15 + 12 + 9 + 14 = 53`, is the 938th name in the list. So,
COLIN would obtain a score of :math:`938 \\times 53 = 49714`.

What is the total of all the name scores in the file?
"""


INPUT_FILENAME = 'p022_names.txt'


class Solution(object):
    def __init__(self, input_filename):
        self._input_filename = input_filename

    def solve(self):
        """
        Load the names into a list with calculated score, sort the list and
        evaluate.
        """
        names = []
        with open(self._input_filename, 'r') as input_file:
            name = ''
            score = 0
            while True:
                c = input_file.read(1)
                if c == '\"':
                    continue
                elif c == ',' or c == '':
                    names.append((name, score))
                    name = ''
                    score = 0
                else:
                    name += c
                    score += ord(c) - ord('A') + 1
                if c == '':
                    break
        total = 0
        i = 0
        for entry in sorted(names):
            i += 1
            total += i * entry[1]
        return total


def main():
    print(Solution(INPUT_FILENAME).solve())


if __name__ == '__main__':
    main()

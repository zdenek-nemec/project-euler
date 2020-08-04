"""
PEP-017: Number letter counts
-----------------------------

Solution for Project Euler problem 17 (https://projecteuler.net/problem=17).

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are :math:`3 + 3 + 5 + 4 + 4 = 19` letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

**NOTE**: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.
"""

TOP = 1000


class ProjectEulerProblem017(object):
    def __init__(self, top):
        self._top = top

    def solve(self):
        """
        Generate names for all the numbers, count the letters and make a sum.
        """
        names = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            30: "thirty",
            40: "forty",
            50: "fifty",
            60: "sixty",
            70: "seventy",
            80: "eighty",
            90: "ninety",
            100: "hundred",
            1000: "thousand"
        }

        total_letters = 0
        for i in range(1, self._top + 1):
            number = i
            number_name = ""
            if number >= 1000:
                number_name += names[number // 1000] + " " + names[1000]
                number %= 1000
                if number < 100 and number != 0:
                    number_name += " and "
                elif number != 0:
                    number_name += " "
            if number >= 100:
                number_name += names[number // 100] + " " + names[100]
                number %= 100
                if number != 0:
                    number_name += " and "
            if number > 20 and number % 10 != 0:
                number_name += (names[number // 10 * 10] +
                                "-" +
                                names[number % 10])
            elif number != 0:
                number_name += names[number]

            letter_count = 0
            for c in number_name:
                if "a" <= c <= "z":
                    letter_count += 1
            total_letters += letter_count

        return total_letters


if __name__ == "__main__":
    print(ProjectEulerProblem017(TOP).solve())

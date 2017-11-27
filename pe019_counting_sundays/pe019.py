#!/usr/bin/env python3

"""
PE019: Counting Sundays
-----------------------

Name: pe019.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe019.py``

Examples:
    ``pe019.py``

Description:
    Solution for Project Euler Problem 19
    (https://projecteuler.net/problem=19).

    You are given the following information, but you may prefer to do some
    research for yourself.

    * 1 Jan 1900 was a Monday.
    * Thirty days has September, April, June and November. All the rest have
      thirty-one, Saving February alone, Which has twenty-eight, rain or
      shine. And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but not on a
      century unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
"""


SEED   = (1900, 1, 1, "Monday")
SEARCH = (0, 0, 1, "Sunday")
START  = (1901, 1, 1)
END    = (2000, 12, 31)


# Solution: Calendar ##########################################################

class Calendar():
    """
    Data structure for solving the issue with generating the calendar.
    """
    def __init__(self, seed, end):
        """
        Generate the calendar.
        """
        self.__names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.__data = [seed]
        self.__extend_to(end)

    def __add_next(self):
        """
        Increase the date according to maximum number of days/months.
        """
        if (self.__get_last_dd() < self.__get_max_dd()):
            self.__data.append((
                self.__get_last_yy(),
                self.__get_last_mm(),
                self.__get_last_dd() + 1,
                self.__names[len(self.__data) % 7]))
        elif (self.__get_last_mm() < 12):
            self.__data.append((
                self.__get_last_yy(),
                self.__get_last_mm() + 1,
                1,
                self.__names[len(self.__data) % 7]))
        else:
            self.__data.append((
                self.__get_last_yy() + 1,
                1,
                1,
                self.__names[len(self.__data) % 7]))

    def __extend_to(self, end):
        """
        Extend the calendar to given date.
        """
        while (self.__get_last()[0:3] < end):
            self.__add_next()

    def __get_last(self):
        """
        Retrieve the last entry (year, month, day, name) from the calendar.
        """
        return (self.__data[len(self.__data) - 1])

    def __get_last_yy(self):
        """
        Retrieve year of the last entry in the calendar.
        """
        return (self.__data[len(self.__data) - 1][0])

    def __get_last_mm(self):
        """
        Retrieve month of the last entry in the calendar.
        """
        return (self.__data[len(self.__data) - 1][1])

    def __get_last_dd(self):
        """
        Retrieve day (number) of the last entry in the calendar.
        """
        return (self.__data[len(self.__data) - 1][2])

    def __get_max_dd(self):
        """
        Calculate maximum number of days of month of the last entry.
        """
        month = self.__get_last_mm()
        if (month == 2):
            year = self.__get_last_yy()
            if (year % 400):
                return 29
            elif (year % 100):
                return 28
            elif (year % 4):
                return 29
            else:
                return 28
        elif ((month == 4) or
            (month == 6) or
            (month == 9) or
            (month == 11)):
            return 30
        else:
            return 31

    def search(self, search, start, end):
        """
        Search for specified key. If value is zero or empty string, ignore it.
        """
        match = []
        for entry in self.__data:
            if (entry[0:3] < start):
                continue
            elif (entry[0:3] > end):
                break
            elif (((entry[0] == search[0]) or (search[0] == 0)) and
                ((entry[1] == search[1]) or (search[1] == 0)) and
                ((entry[2] == search[2]) or (search[2] == 0)) and
                ((entry[3] == search[3]) or (search[3] == ""))):
                match.append(entry)
        return match

    def print_data(self):
        """
        Print the whole generated calendar.
        """
        i = 0
        for entry in self.__data:
            print(i, ":", entry)
            i += 1

def solve_calendar(seed, search, start, end):
    """
    Generate the calendar from the seed to the end date. Search for the given
    key.
    """
    cal = Calendar(seed, end)
    # cal.print_data()
    return len(cal.search(search, start, end))


# Main ########################################################################

def main():
    result = solve_calendar(SEED, SEARCH, START, END)
    print("Solution: Calendar")
    print("\tNumber of Sundays that fell on the first of the month during the twentieth century is", result)

    return 0


if __name__ == "__main__":
    main()

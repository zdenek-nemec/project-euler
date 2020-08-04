"""
PEP-019: Counting Sundays
-------------------------

Solution for Project Euler problem 19 (https://projecteuler.net/problem=19).

You are given the following information, but you may prefer to do some research
for yourself.

* 1 Jan 1900 was a Monday.
* Thirty days has September, April, June and November. All the rest have
  thirty-one, Saving February alone, Which has twenty-eight, rain or shine. And
  on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""

SEED = (1900, 1, 1, "Monday")
SEARCH = (0, 0, 1, "Sunday")
START = (1901, 1, 1)
END = (2000, 12, 31)


class Calendar(object):
    def __init__(self, seed, end):
        self._names = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]
        self._data = [seed]
        self._extend_to(end)

    def _add_next(self):
        """
        Increase the date according to maximum number of days/months.
        """
        if self._get_last_day() < self._get_max_day():
            self._data.append((
                self._get_last_year(),
                self._get_last_month(),
                self._get_last_day() + 1,
                self._names[len(self._data) % 7]))
        elif self._get_last_month() < 12:
            self._data.append((
                self._get_last_year(),
                self._get_last_month() + 1,
                1,
                self._names[len(self._data) % 7]))
        else:
            self._data.append((
                self._get_last_year() + 1,
                1,
                1,
                self._names[len(self._data) % 7]))

    def _extend_to(self, end):
        """
        Extend the calendar to given date.
        """
        while self._get_last()[0:3] < end:
            self._add_next()

    def _get_last(self):
        """
        Retrieve the last entry (year, month, day, name) from the calendar.
        """
        return self._data[len(self._data) - 1]

    def _get_last_day(self):
        """
        Retrieve day (number) of the last entry in the calendar.
        """
        return self._data[len(self._data) - 1][2]

    def _get_last_month(self):
        """
        Retrieve month of the last entry in the calendar.
        """
        return self._data[len(self._data) - 1][1]

    def _get_last_year(self):
        """
        Retrieve year of the last entry in the calendar.
        """
        return self._data[len(self._data) - 1][0]

    def _get_max_day(self):
        """
        Calculate maximum number of days of month of the last entry.
        """
        month = self._get_last_month()
        if month == 2:
            year = self._get_last_year()
            if year % 400:
                return 29
            elif year % 100:
                return 28
            elif year % 4:
                return 29
            else:
                return 28
        elif (month == 4 or
              month == 6 or
              month == 9 or
              month == 11):
            return 30
        else:
            return 31

    def print_data(self):
        """
        Print the whole generated calendar.
        """
        i = 0
        for entry in self._data:
            print(i, ":", entry)
            i += 1

    def search(self, search, start, end):
        """
        Search for specified key. If value is zero or empty string, ignore it.
        """
        match = []
        for entry in self._data:
            if entry[0:3] < start:
                continue
            elif entry[0:3] > end:
                break
            elif ((entry[0] == search[0] or search[0] == 0) and
                  (entry[1] == search[1] or search[1] == 0) and
                  (entry[2] == search[2] or search[2] == 0) and
                  (entry[3] == search[3] or search[3] == '')):
                match.append(entry)
        return match


class ProjectEulerProblem019(object):
    def __init__(self, seed, search, start, end):
        self._seed = seed
        self._search = search
        self._start = start
        self._end = end

    def solve(self):
        """
        Generate the calendar from the seed to the end date. Search for the
        given key.
        """
        calendar = Calendar(self._seed, self._end)
        return len(calendar.search(self._search, self._start, self._end))


if __name__ == "__main__":
    print(ProjectEulerProblem019(SEED, SEARCH, START, END).solve())

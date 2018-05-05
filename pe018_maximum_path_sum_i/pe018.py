#!/usr/bin/env python3

"""
PE-018: Maximum path sum I
--------------------------

Solution for Project Euler Problem 18 (https://projecteuler.net/problem=18).

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

.. code-block:: none

       3
      7 4
     2 4 6
    8 5 9 3

..

That is, :math:`3 + 7 + 4 + 9 = 23`.

Find the maximum total from top to bottom of the triangle below:

.. code-block:: none

                  75
                 95 64
                17 47 82
               18 35 87 10
              20 04 82 47 65
             19 01 23 75 03 34
            88 02 77 73 07 63 67
           99 65 04 28 06 16 70 92
          41 41 26 56 83 40 80 70 33
         41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
       70 11 33 28 77 73 17 78 39 68 17 57
      91 71 52 38 17 14 91 43 58 50 27 29 48
     63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

**NOTE**: As there are only 16384 routes, it is possible to solve this problem
by trying every route. However, Problem 67, is the same challenge with a
triangle containing one-hundred rows; it cannot be solved by brute force, and
requires a clever method! ;o)
"""


import csv


INPUT_FILENAME = 'triangle_big.txt'


class TriangleBottomUp(object):
    def __init__(self, filename):
        self._data = []
        self._x = 0
        self._y = 0
        self.load_data(filename)

    def check_last_node(self):
        """
        Determine whether the node is last in selected level.
        """
        if self._x == (len(self._data[self._y])) - 1:
            return True
        return False

    def check_root(self):
        """
        Determine whether the node is root of the triangle.
        """
        if self._x == 0 and self._y == 0:
            return True
        return False

    def focus_last_level(self):
        """
        Select last (bottom) level of the triangle, first element.
        """
        self._x = 0
        self._y = len(self._data) - 1

    def focus_next_node(self):
        """
        Select next element in the current level of the triangle.
        """
        self._x += 1

    def focus_previous_level(self):
        """
        Select previous (upper) level of the triangle, first element.
        """
        self._x = 0
        self._y -= 1

    def get_current(self):
        """
        Retrieve a number that is in focus.
        """
        return int(self._data[self._y][self._x])

    def get_left_leaf(self):
        """
        Retrieve a number that is in left leaf of focused node.
        """
        return int(self._data[self._y + 1][self._x])

    def get_right_leaf(self):
        """
        Retrieve a number that is in right leaf of focused node.
        """
        return int(self._data[self._y + 1][self._x + 1])

    def load_data(self, filename):
        """
        Load the triangle data into the structure from given file.
        """
        with open(filename) as csv_file:
            reader = csv.reader(csv_file, delimiter=' ')
            for row in reader:
                self._data.append(row)

    def update(self, value):
        """
        Update the value of selected node.
        """
        self._data[self._y][self._x] = str(value)


class Solution(object):
    def __init__(self, filename):
        self._filename = filename

    def solve(self):
        """
        Go from the bottom of the triangle upwards. Update each node with a sum
        of his value and greater value of his leaves. After reaching root of the
        triangle, return its updated value.
        """
        triangle = TriangleBottomUp(self._filename)
        triangle.focus_last_level()
        while True:
            if triangle.check_root():
                break
            triangle.focus_previous_level()
            while True:
                triangle.update(
                    triangle.get_current() + max(
                        triangle.get_left_leaf(),
                        triangle.get_right_leaf()))
                if triangle.check_last_node():
                    break
                triangle.focus_next_node()
        return triangle.get_current()


def main():
    print(Solution(INPUT_FILENAME).solve())


if __name__ == '__main__':
    main()

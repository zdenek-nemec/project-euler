#!/usr/bin/env python3

"""
PE018: Maximum path sum I
-------------------------

Name: pe018.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe018.py``

Examples:
    ``pe018.py``

Description:
    Solution for Project Euler Problem 18
    (https://projecteuler.net/problem=18).

    By starting at the top of the triangle below and moving to adjacent
    numbers on the row below, the maximum total from top to bottom is 23.

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

.. note::
    As there are only 16384 routes, it is possible to solve this problem
    by trying every route. However, Problem 67, is the same challenge with
    a triangle containing one-hundred rows; it cannot be solved by brute
    force, and requires a clever method! ;o)
"""


import csv


# INPUT_FILE = "triangle_small.txt"
INPUT_FILE = "triangle_big.txt"


# Solution: Brute Force #######################################################

class TriangleBF():
    """
    Data structure for solving the triangle sum with brute force.
    """
    def __init__(self, filename):
        self.__data = self.load_data(filename)
        self.__x = 0
        self.__y = 0

    def get_current(self):
        """
        Retrieve a number that is in focus.
        """
        return (int(self.__data[self.__y][self.__x]))

    def get_size(self):
        """
        Retrieve size (length/width) if the triangle.
        """
        return (len(self.__data))

    def load_data(self, filename):
        """
        Load the triangle data into the structure from given file.
        """
        data = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter = ' ')
            for row in reader:
                data.append(row)
        return data

    def move_left(self):
        """
        Move the focus down-left.
        """
        # self.__x = self.__x
        self.__y += 1

    def move_right(self):
        """
        Move the focus down-right.
        """
        self.__x += 1
        self.__y += 1

    def reset_focus(self):
        """
        Reset the focus to the root.
        """
        self.__x = 0
        self.__y = 0


def solve_brute_force(filename):
    """
    Explore all the possible routes from top to bottow, calculate sums of all
    the paths and select the greatest.
    """
    triangle = TriangleBF(filename)
    steps = triangle.get_size() - 1
    sums = []
    for path in range(0, (2 ** steps)):
        triangle.reset_focus()
        path_sum = triangle.get_current()
        # print path, ":", triangle.get_current(),
        for step in range(0, steps):
            if (path & ((2 ** (steps - 1)) >> step)):
                triangle.move_right()
            else:
                triangle.move_left()
            path_sum += triangle.get_current()
            # print "+", triangle.get_current(),
        sums.append(path_sum)
        # print "=", path_sum

    return max(sums)


# Solution: Bottom-Up #########################################################

class TriangleBU():
    """
    Data structure for solving the triangle sum with bottom-up algorithm.
    """
    def __init__(self, filename):
        self.__data = self.load_data(filename)
        self.__x = 0
        self.__y = 0

    def focus_last_level(self):
        """
        Select last (bottom) level of the triangle, first element.
        """
        self.__x = 0
        self.__y = len(self.__data) - 1

    def focus_next_node(self):
        """
        Select next element in the current level of the triangle.
        """
        self.__x += 1

    def focus_prev_level(self):
        """
        Select previous (upper) level of the triangle, first element.
        """
        self.__x = 0
        self.__y -= 1

    def get_current(self):
        """
        Retrieve a number that is in focus.
        """
        return (int(self.__data[self.__y][self.__x]))

    def get_left_leaf(self):
        """
        Retrieve a number that is in left leaf of focused node.
        """
        return (int(self.__data[self.__y + 1][self.__x]))

    def get_right_leaf(self):
        """
        Retrieve a number that is in right leaf of focused node.
        """
        return (int(self.__data[self.__y + 1][self.__x + 1]))

    def check_last_node(self):
        """
        Determine whether the node is last in selected level.
        """
        if (self.__x == (len(self.__data[self.__y])) - 1):
            return True
        return False

    def check_root(self):
        """
        Determine whether the node is root of the triangle.
        """
        if ((self.__x == 0) and (self.__y == 0)):
            return True
        return False

    def load_data(self, filename):
        """
        Load the triangle data into the structure from given file.
        """
        data = []
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter = ' ')
            for row in reader:
                data.append(row)
        return data

    def update(self, value):
        """
        Update the value of selected node.
        """
        self.__data[self.__y][self.__x] = str(value)


def solve_bottom_up(filename):
    """
    Go from bottom of the triangle upwards. Update each node with a sum of his
    value and greater value of his leaves. After reaching root of the
    triangle, return its updated value.
    """
    triangle = TriangleBU(filename)
    triangle.focus_last_level()
    while (1):
        if (triangle.check_root()):
            break
        triangle.focus_prev_level()
        while (1):
            triangle.update(triangle.get_current() + max(triangle.get_left_leaf(), triangle.get_right_leaf()))
            if (triangle.check_last_node()):
                break
            triangle.focus_next_node()

    return triangle.get_current()


# Main ########################################################################

def main():
    result = solve_brute_force(INPUT_FILE)
    print("Solution: Brute Force")
    print("\tThe maximum total from top to bottom of the triangle is", result)

    result = solve_bottom_up(INPUT_FILE)
    print("Solution: Bottom-Up")
    print("\tThe maximum total from top to bottom of the triangle is", result)

    return 0


if __name__ == "__main__":
    main()

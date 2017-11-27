#!/usr/bin/env python3

"""
PE015: Lattice paths
--------------------

Name: pe015.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-27)

Synopsis:
    ``pe015.py``

Examples:
    ``pe015.py``

Description:
    Solution for Project Euler Problem 15
    (https://projecteuler.net/problem=15).

    Starting in the top left corner of a 2x2 grid, and only being able to move
    to the right and down, there are exactly 6 routes to the bottom right
    corner.

.. image:: /pe015_lattice_paths/p015.gif
    :align: center

..

    How many such routes are there through a 20x20 grid?
"""


DIM_X = 20
DIM_Y = 20


# Solution: Brute Force #######################################################

def solve_matrix(x, y):
    matrix = []
    for i in range(0, x+1):
        matrix.append([])
        for j in range(0, y+1):
            if ((i == 0) or (j == 0)):
                matrix[i].append(1)
            else:
                matrix[i].append(matrix[i][j-1] + matrix[i-1][j])
    return (matrix[x][y])


# Main ########################################################################

def main():
    result = solve_matrix(DIM_X, DIM_Y)
    print("Solution: Matrix")
    print("\tThe number of routes in a", DIM_X, "x", DIM_Y, "grid is", result)

    return 0


if __name__ == "__main__":
    main()

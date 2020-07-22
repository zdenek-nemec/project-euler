"""
PEP-015: Lattice paths
----------------------

Solution for Project Euler problem 15 (https://projecteuler.net/problem=15).

Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

.. image:: /problems_0xx/pep015_lattice_paths/p015.gif
    :align: center

..

How many such routes are there through a 20x20 grid?
"""

SIZE_X = 20
SIZE_Y = 20


class ProjectEulerProblem015(object):
    def __init__(self, size_x, size_y):
        self._size_x = size_x
        self._size_y = size_y

    def solve(self):
        matrix = []
        for x in range(0, self._size_x + 1):
            matrix.append([])
            for y in range(0, self._size_y + 1):
                if x == 0 or y == 0:
                    matrix[x].append(1)
                else:
                    matrix[x].append(matrix[x][y - 1] + matrix[x - 1][y])
        return matrix[self._size_x][self._size_y]


if __name__ == "__main__":
    print(ProjectEulerProblem015(SIZE_X, SIZE_Y).solve())

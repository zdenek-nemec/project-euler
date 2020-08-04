"""
PEP-375: Minimum of subsequences
--------------------------------

Solution for Project Euler problem 375 (https://projecteuler.net/problem=375).

Let :math:`S_{n}` be an integer sequence produced with the following
pseudo-random number generator:

.. math::

    S_{0} &= 290797

    S_{n+1} &= {S_{n}}^{2} \\text{ mod } 50515093

..

Let :math:`A(i,j)` be the minimum of the numbers
:math:`S_{i}, S_{i+1}, ..., S_{j}` for :math:`i \\leq j`.

Let :math:`M(N) = \\sum A(i,j)` for :math:`1 \\leq i \\leq j \\leq N`.

We can verify that :math:`M(10) = 432256955` and
:math:`M(10 \\ 000) = 3264567774119`.

Find :math:`M(2 \\ 000 \\ 000 \\ 000)`.

.. warning:: Open
"""


class ProjectEulerProblem375(object):
    def solve(self):
        return 0


if __name__ == "__main__":
    print(ProjectEulerProblem375().solve())

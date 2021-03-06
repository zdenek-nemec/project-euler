"""
PEP-030: Digit fifth powers
---------------------------

Solution for Project Euler problem 30 (https://projecteuler.net/problem=30).

Surprisingly there are only three numbers that can be written as the sum of
fourth powers of their digits:

.. math::

    1634 &= 1^4 + 6^4 + 3^4 + 4^4

    8208 &= 8^4 + 2^4 + 0^4 + 8^4

    9474 &= 9^4 + 4^4 + 7^4 + 4^4

..

As :math:`1 = 1^4` is not a sum it is not included.

The sum of these numbers is :math:`1634 + 8208 + 9474 = 19316`.

Find the sum of all the numbers that can be written as the sum of fifth powers
of their digits.

.. warning:: Open
"""


class ProjectEulerProblem030(object):
    def solve(self):
        return 0


if __name__ == "__main__":
    print(ProjectEulerProblem030().solve())

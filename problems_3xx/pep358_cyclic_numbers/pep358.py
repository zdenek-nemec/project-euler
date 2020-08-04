"""
PEP-358: Cyclic numbers
-----------------------

Solution for Project Euler problem 358 (https://projecteuler.net/problem=358).

A **cyclic number** with :math:`n` digits has a very interesting property:

When it is multiplied by :math:`1, 2, 3, 4, ... n`, all the products have
exactly the same digits, in the same order, but rotated in a circular fashion!

The smallest cyclic number is the 6-digit number 142857:

.. math::

    142857 \\times 1 &= 142857

    142857 \\times 2 &= 285714

    142857 \\times 3 &= 428571

    142857 \\times 4 &= 571428

    142857 \\times 5 &= 714285

    142857 \\times 6 &= 857142

..

The next cyclic number is 0588235294117647 with 16 digits:

.. math::

    0588235294117647 \\times 1 &= 0588235294117647

    0588235294117647 \\times 2 &= 1176470588235294

    0588235294117647 \\times 3 &= 1764705882352941

    ...

    0588235294117647 \\times 16 &= 9411764705882352

..

Note that for cyclic numbers, leading zeros are important.

There is only one cyclic number for which, the eleven leftmost digits are
00000000137 and the five rightmost digits are 56789 (i.e., it has the form
00000000137...56789 with an unknown number of digits in the middle). Find the
sum of all its digits.

.. warning:: Open
"""


class ProjectEulerProblem358(object):
    def solve(self):
        return 0


if __name__ == "__main__":
    print(ProjectEulerProblem358().solve())

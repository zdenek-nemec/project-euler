"""
PE-000: Template
----------------

Solution for Project Euler problem 0 (https://projecteuler.net/problem=0).

This is just a template, nothing more. Now go away.

.. warning:: Open
"""

LUCKY_NUMBER = 7


class ProjectEulerProblem000(object):
    def __init__(self, lucky_number):
        self._lucky_number = lucky_number

    def solve(self):
        return self._lucky_number


def main():
    print(ProjectEulerProblem000(LUCKY_NUMBER).solve())


if __name__ == "__main__":
    main()

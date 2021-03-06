"""
PEP-016: Power digit sum
------------------------

Solution for Project Euler problem 16 (https://projecteuler.net/problem=16).

:math:`2^{15} = 32768` and the sum of its digits is
:math:`3 + 2 + 7 + 6 + 8 = 26`.

What is the sum of the digits of the number :math:`2^{1000}`?
"""

POWER = 1000


class ProjectEulerProblem016(object):
    def __init__(self, power):
        self._power = power

    def solve(self):
        number = pow(2, self._power)
        number_string = str(number)
        power_sum = 0
        for c in number_string:
            power_sum += int(c)
        return power_sum


if __name__ == "__main__":
    print(ProjectEulerProblem016(POWER).solve())

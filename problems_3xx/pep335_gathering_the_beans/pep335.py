"""
PEP-335: Gathering the beans
----------------------------

Solution for Project Euler problem 335 (https://projecteuler.net/problem=335).

Whenever Peter feels bored, he places some bowls, containing one bean each, in a
circle. After this, he takes all the beans out of a certain bowl and drops them
one by one in the bowls going clockwise. He repeats this, starting from the bowl
he dropped the last bean in, until the initial situation appears again. For
example with 5 bowls he acts as follows:

.. image:: /problems_3xx/pep335_gathering_the_beans/p335_mancala.gif
    :align: center

..

So with 5 bowls it takes Peter 15 moves to return to the initial situation.

Let :math:`M(x)` represent the number of moves required to return to the initial
situation, starting with :math:`x` bowls. Thus, :math:`M(5) = 15`. It can also
be verified that :math:`M(100) = 10920`.

Find :math:`\sum_{k=0}^{10^{18}} M(2^k + 1)`. Give your answer modulo
:math:`7^9`.

.. warning:: Open
"""


class ProjectEulerProblem335(object):
    def solve(self):
        return 0


if __name__ == "__main__":
    print(ProjectEulerProblem335().solve())

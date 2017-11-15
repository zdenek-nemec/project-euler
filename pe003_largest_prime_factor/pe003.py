#!/usr/bin/env python

"""
PE003: Largest prime factor
---------------------------

Name: pe003.py

Author: Zdenek Nemec <zdenek.nemec@artin.cz>

Version: 2.0 (2017-11-15)

Synopsis:
    ``pe003.py``

Examples:
    ``pe003.py``

Description:
    Solution for Project Euler problem 3 (https://projecteuler.net/problem=3).

    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143?
"""


NUMBER = 600851475143


# Solution: Factors of factors ################################################

class Factors(object):
    def __init__(self):
        pass

    @staticmethod
    def get_factors(number):
        factors = []
        possible_factor = 2
        cap = number / 2
        while possible_factor <= cap:
            if number % possible_factor == 0:
                factors.append(possible_factor)
                factors.append(number / possible_factor)
            possible_factor += 1
            cap = number / possible_factor
        factors.sort()
        return factors

    def get_prime_factors(self, number):
        factors = self.get_factors(number)
        prime_factors = []
        for possible_prime in factors:
            if not(self.get_factors(possible_prime)):
                prime_factors.append(possible_prime)
        prime_factors.sort()
        return prime_factors

    def get_largest_prime_factor(self, number):
        prime_factors = self.get_prime_factors(number)
        return prime_factors[-1]


# Main ########################################################################

def main():
    print Factors().get_largest_prime_factor(NUMBER)


if __name__ == "__main__":
    main()

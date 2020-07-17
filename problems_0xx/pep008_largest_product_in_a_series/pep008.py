"""
PEP-008: Largest product in a series
------------------------------------

Solution for Project Euler problem 8 (https://projecteuler.net/problem=8).

The four adjacent digits in the 1000-digit number that have the greatest product
are :math:`9 \\times 9 \\times 8 \\times 9 = 5832`.

| 73167176531330624919225119674426574742355349194934
| 96983520312774506326239578318016984801869478851843
| 85861560789112949495459501737958331952853208805511
| 12540698747158523863050715693290963295227443043557
| 66896648950445244523161731856403098711121722383113
| 62229893423380308135336276614282806444486645238749
| 30358907296290491560440772390713810515859307960866
| 70172427121883998797908792274921901699720888093776
| 65727333001053367881220235421809751254540594752243
| 52584907711670556013604839586446706324415722155397
| 53697817977846174064955149290862569321978468622482
| 83972241375657056057490261407972968652414535100474
| 82166370484403199890008895243450658541227588666881
| 16427171479924442928230863465674813919123162824586
| 17866458359124566529476545682848912883142607690042
| 24219022671055626321111109370544217506941658960408
| 07198403850962455444362981230987879927244284909188
| 84580156166097919133875499200524063689912560717606
| 05886116467109405077541002256983155200055935729725
| 71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""

INPUT_FILENAME = "number.txt"
DIGITS = 13


class ProjectEulerProblem008(object):
    def __init__(self, input_filename, digits):
        self._input_filename = input_filename
        self._digits = digits

    def solve(self):
        number = []
        with open(self._input_filename, "r") as input_file:
            while True:
                c = input_file.read(1)
                if c < "0" or c > "9":
                    break
                number.append(int(c))
        assert len(number) == 1000, "Number is expected to have 1000 digits."

        max_product = 0
        product_index = 0
        while True:
            if product_index + self._digits > len(number):
                break
            product = number[product_index]
            for series_index in range(1, self._digits):
                # Optimisation: Zero product
                if number[product_index + series_index] == 0:
                    product = 0
                    break
                product *= number[product_index + series_index]
            if product > max_product:
                max_product = product
            product_index += 1

        return max_product


def main():
    print(ProjectEulerProblem008(INPUT_FILENAME, DIGITS).solve())


if __name__ == "__main__":
    main()

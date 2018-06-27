import math


class Divisors(object):
    @staticmethod
    def get_divisors(number):
        divisors = [1]
        for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                divisors.append(divisor)
                if number // divisor not in divisors:
                    divisors.append(number // divisor)
        return sorted(divisors)


def main():
    print('Hello World!')


if __name__ == '__main__':
    main()

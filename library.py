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


class Fibonacci(object):
    def __init__(self, start):
        self._series = start

    def append_next(self):
        next_number = self._series[-2] + self._series[-1]
        self._series.append(next_number)

    def get_all(self):
        return self._series

    def get_last(self):
        return self._series[-1]

    def get_length(self):
        return len(self._series)


def main():
    print('Hello World!')


if __name__ == '__main__':
    main()

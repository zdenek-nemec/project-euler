import math


class Divisors(object):
    def __init__(self):
        self._divisors = {}

    def _calculate_divisors(self, number):
        divisors = [1]
        for divisor in range(2, int(math.sqrt(number)) + 1):
            if number % divisor == 0:
                divisors.append(divisor)
                if number // divisor not in divisors:
                    divisors.append(number // divisor)
        return sorted(divisors)

    def _save_divisors(self, number, divisors):
        self._divisors[number] = divisors

    def get_divisors(self, number):
        if number not in self._divisors:
            divisors = self._calculate_divisors(number)
            self._save_divisors(number, divisors)
        return self._divisors[number]



class Fibonacci(object):
    def __init__(self, start=(1, 1)):
        self._series = list(start)

    def append_next(self):
        next_number = self._series[-1] + self._series[-2]
        self._series.append(next_number)

    def get_series(self):
        return self._series

    def get_last(self):
        return self._series[-1]

    def get_length(self):
        return len(self._series)


if __name__ == '__main__':
    pass

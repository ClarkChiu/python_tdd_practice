from functools import reduce

class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x * y, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return 'inf'

    def avg(self, numbers, ut=None):
        if not ut:
            ut = max(numbers)

        new_list = [x for x in numbers if x <= ut]

        return sum(new_list)/len(new_list)

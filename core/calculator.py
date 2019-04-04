""" Calculator module """


class Calculator:
    """ Calculator to perform various math operations """

    def __init__(self, starting_total=0):
        self._total = starting_total

    @property
    def total(self):
        """ return the calculator instance's running total """
        return self._total

    def add(self, num):
        """ returns the sum of the current total and num """
        self._total += num
        return self.total

    def subtract(self, num):
        """ returns the difference between the current total and num """
        self._total -= num
        return self.total

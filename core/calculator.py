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
        """ returns the sum of x and y """
        self._total += num
        return self.total

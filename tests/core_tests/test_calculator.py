""" Tests for the calculator module """
from core.calculator import Calculator


class TestCalculator:
    """ Tests for the Calculator class """

    calculator = Calculator()

    def setup_method(self):
        """ start each test with a fresh Calculator instance """
        self.calculator = Calculator()

    def test_add(self):
        """ test the add method of Calculator """
        num = 10
        expected_sum = 0 + 10
        result = self.calculator.add(num)
        assert result == expected_sum

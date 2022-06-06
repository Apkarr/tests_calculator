import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_correctly(self):
        assert self.calc.multiply(self, 6, 8) == 48

    def test_division_correctly(self):
        assert self.calc.division(self, 36, 9) == 4

    def test_subtraction_correctly(self):
        assert self.calc.subtraction(self, 56, 13) == 43

    def test_adding_corrently(self):
        assert self.calc.adding(self, 3, 9) == 12

import pytest

from app.calc import Calculator

class TestCalculator:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 2, 2) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 20, 5) == 15

    def test_division(self):
         assert self.calc.division(self, 50, 2) == 25

    def test_multiply(self):
        assert self.calc.multiply(self, 32, 2) == 64

    def teardown(self):
        print('Выполнения метода Teardown')
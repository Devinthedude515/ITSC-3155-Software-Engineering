import unittest
import os
print(os.getcwd())
from pyunitActivityDevinWilliams.calculator import Calculator

class TestCalculator(unittest.TestCase):

    #test add method
    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(5, 0), 5)
    #test sub method
    def test_sub(self):
        calculator = Calculator()
        self.assertEqual(calculator.sub(3, 2), 1)
        self.assertEqual(calculator.sub(4, 1), 3)
    #test mul method
    def test_mul(self):
        calculator = Calculator()
        self.assertEqual(calculator.mul(1, 2), 2)
        self.assertEqual(calculator.mul(2, 2), 4)
    #test div method
    def test_div(self):
        calculator = Calculator()
        self.assertEqual(calculator.div(2, 2), 1)
        self.assertEqual(calculator.div(6, 2), 3)

if __name__ == '__main__':
    unittest.main()
# TO MAKE TESTS 
import unittest
import logging

# TO IMPORT TEST FILE
import sys 
sys.path.append('')

# TO test 
from ex1 import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    
    def test_add(self):
        # 2 entiers positifs
        result = self.calculator.add(2, 2)
        self.assertEqual(result, 4)

        # 2 zeros
        result = self.calculator.add(0, 0)
        self.assertEqual(result, 0)

        # 2 entiers négatifs
        result = self.calculator.add(-2, -2)
        self.assertEqual(result, -4)

        # 1 entier positif et 1 entier négatif
        result = self.calculator.add(2, -2)
        self.assertEqual(result, 0)

        # 1 entier négatif et 1 entier positif
        result = self.calculator.add(-2, 2)
        self.assertEqual(result, 0)

        # Avec modification de la fonction pour que les paramètres ne soient que des nombres (entiers ou flotants)
        result = self.calculator.add("2", "2")
        self.assertEqual(result, "Invalid input: both arguments must be numbers.")


    def test_subtract(self):
        # 2 entiers positifs
        result = self.calculator.subtract(2, 2)
        self.assertEqual(result, 0)

        # 2 zeros
        result = self.calculator.subtract(0, 0)
        self.assertEqual(result, 0)

        # 2 entiers négatifs
        result = self.calculator.subtract(-2, -2)
        self.assertEqual(result, 0)

        # 1 entier positif et 1 entier négatif
        result = self.calculator.subtract(2, -2)
        self.assertEqual(result, 4)

        # 1 entier négatif et 1 entier positif
        result = self.calculator.subtract(-2, 2)
        self.assertEqual(result, -4)

        # Avec modification de la fonction pour que les paramètres ne soient que des nombres (entiers ou flotants)
        result = self.calculator.subtract("2", "2")
        self.assertEqual(result, "Invalid input: both arguments must be numbers.")
    
    def test_multiply(self):
        # 2 entiers positifs
        result = self.calculator.multiply(2, 2)
        self.assertEqual(result, 4)

        # 2 zeros
        result = self.calculator.multiply(0, 0)
        self.assertEqual(result, 0)

        # 2 entiers négatifs
        result = self.calculator.multiply(-2, -2)
        self.assertEqual(result, 4)

        # 1 entier positif et 1 entier négatif
        result = self.calculator.multiply(2, -2)
        self.assertEqual(result, -4)

        # 1 entier négatif et 1 entier positif
        result = self.calculator.multiply(-2, 2)
        self.assertEqual(result, -4)

        # Avec modification de la fonction pour que les paramètres ne soient que des nombres (entiers ou flotants)
        result = self.calculator.multiply("2", "2")
        self.assertEqual(result, "Invalid input: both arguments must be numbers.")
    
    def test_divide(self):
        # 2 entiers positifs
        result = self.calculator.divide(2, 2)
        self.assertEqual(result, 1)

        # 2 zeros
        result = self.calculator.divide(0, 0)
        self.assertEqual(result, "Invalid input: division by zero.")

        # 1 entier et 1 zero
        result = self.calculator.divide(1, 0)
        self.assertEqual(result, "Invalid input: division by zero.")

        # 1 zero et 1 entier
        result = self.calculator.divide(0, 2)
        self.assertEqual(result, 0)

        # 2 entiers négatifs
        result = self.calculator.divide(-2, -2)
        self.assertEqual(result, 1)

        # 1 entier positif et 1 entier négatif
        result = self.calculator.divide(2, -2)
        self.assertEqual(result, -1)

        # 1 entier négatif et 1 entier positif
        result = self.calculator.divide(-2, 2)
        self.assertEqual(result, -1)

        # Avec modification de la fonction pour que les paramètres ne soient que des nombres (entiers ou flotants)
        result = self.calculator.divide("2", "2")
        self.assertEqual(result, "Invalid input: both arguments must be numbers.")
    
    def test_power(self):
        # 2^2 = 4 
        result = self.calculator.power(2, 2)
        self.assertEqual(result, 4)

        # 1^0 = 1 
        result = self.calculator.power(1, 0)
        self.assertEqual(result, 1)

        # 0^0 = 0 
        result = self.calculator.power(0, 0)
        self.assertEqual(result, 1)

        # 0^1 = 0 
        result = self.calculator.power(0, 1)
        self.assertEqual(result, 0)

        # 1^-2 = 1 / 1 = 1 
        result = self.calculator.power(1, -2)
        self.assertEqual(result, 1)

        # 2^-2 = 1 / 4 = 0.25 
        result = self.calculator.power(2, -2)
        self.assertEqual(result, 0.25)

        result = self.calculator.power(-5, -5)
        self.assertEqual(result, -0.00032)

        # Avec modification de la fonction pour que les paramètres ne soient que des nombres (entiers ou flotants)
        result = self.calculator.power("2", "2")
        self.assertEqual(result, "Invalid input: both arguments must be numbers.")
    
    def test_square_root(self):
        result = self.calculator.square_root(4)
        self.assertEqual(round(result), 2)

        result = self.calculator.square_root(0)
        self.assertEqual(result, 0)

        result = self.calculator.square_root(1)
        self.assertEqual(result, 1)

        result = self.calculator.square_root(3)
        self.assertEqual(result, 1.7320508100147274)

        result = self.calculator.square_root(0.25)
        self.assertEqual(result, 0.5000000232305737)

        result = self.calculator.square_root(-1)
        self.assertEqual(result, "Invalid input: division by zero.")

        # Avec modification de la fonction pour que les paramètres ne soient que des nombres (entiers ou flotants)
        result = self.calculator.square_root("2")
        self.assertEqual(result, 'Invalid input: both arguments must be numbers.')

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr)
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
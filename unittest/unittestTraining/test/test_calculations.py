import sys
import unittest

from src.calculations import add, sub, mul, div, ne

class TestCalculations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(15, add(10,5), msg='Addition Err')

    def test_sub(self):
        self.assertEqual(5, sub(10,5), msg='Subtraction Err')

    def test_mul(self):
        self.assertEqual(50, mul(10,5), msg='Multiplication Err')

    def test_div(self):
        self.assertEqual(2.0, div(10,5), msg='Division Err')

    def test_ne(self):
        self.assertFalse(ne(10,10))
        self.assertTrue(ne(10,5))

    def test_diverr(self):
        with self.assertRaises(ZeroDivisionError):
            div(10,0)

if __name__ == "__main__":
    unittest.main()
# python -m unittest tests/test_checker.py
import unittest
from is_odd import is_odd

class TestIsOdd(unittest.TestCase):
    def test_odd_numbers(self):
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(5))
        self.assertTrue(is_odd(-7))

    def test_even_numbers(self):
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(4))
        self.assertFalse(is_odd(-6))

if __name__ == '__main__':
    unittest.main()
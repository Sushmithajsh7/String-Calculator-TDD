import unittest
from src.calculator import add

# Test Cases to check the add functionality
class testStringCalculator(unittest.TestCase):
    def test_emptyString(self):
        self.assertEqual(add(""), 0)




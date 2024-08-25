import unittest
from src.calculator import add

# Test Cases to check the add functionality
class testStringCalculator(unittest.TestCase):

    # test case for an empty string
    def test_emptyString(self):
        self.assertEqual(add(""), 0)

    # test case to take any number of inputs with comma as a delimiter
    def test_inputNumber(self):
        self.assertEqual(add("1,2,3"), 6)

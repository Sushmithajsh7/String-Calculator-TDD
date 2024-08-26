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

    # test case to consider new line character between numbers instead of comma
    def test_newLine(self):
        self.assertEqual(add("1\n2,3"), 6)

    #test case to handle different delimiters
    def test_differentDelimiters(self):
        self.assertEqual(add("//;\n1;2"), 3)

    # test case to raise an error if negative number is given as an input
    def test_negativeInput(self):
        with self.assertRaises(ValueError) as context:
            add("//;\n-1;-2;-6;9")
        self.assertEqual(str(context.exception), "negative numbers not allowed [-1, -2, -6]")

    #test case to handle numbers bigger than 1000
    def test_biggerNumbers(self):
        self.assertEqual(add("2,1001"), 2)

    #test case to handle delimiters of any length
    def test_lengthierDelimiter(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_multipleDelimiters(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)




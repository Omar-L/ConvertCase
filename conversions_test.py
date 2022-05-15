from cgitb import reset
import unittest
from conversions import Conversions as c

class TestConversions(unittest.TestCase):
    def test_upper_case(self):
        result = c.upper_case('test')
        self.assertEqual(result, "TEST")

    def test_lower_case(self):
        result = c.lower_case('TEST')
        self.assertEqual(result, "test")        

    def test_title_case(self):
        result = c.title_case('mad max: fury road')
        self.assertEqual(result, "Mad Max: Fury Road")

    def test_capital_case(self):
        result = c.capital_case('hi, are you new here?')
        self.assertEqual(result, "Hi, are you new here?")

    def test_alternating_case(self):
        result = c.alternating_case("i don't test my code")
        self.assertEqual(result, "i dOn't tEsT My cOdE")

    def test_all(self):
        result = c.all('this is a test')
        converted_list = ['THIS IS A TEST', 'this is a test', 'This Is A Test', 'This is a test', 'tHiS Is a tEsT']
        self.assertListEqual(result, converted_list)

if __name__ == '__main__':
    unittest.main()
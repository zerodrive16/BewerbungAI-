import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from WebApplication.Text_Preprocessing.regex_processing import *

class RegexProcessingTest(unittest.TestCase):

    def test_remove_emojis_and_unicode(self):
        input_text = "Bewerbung 😊 AI 🌍!"
        expected_output = "Bewerbung AI !"
        self.assertEqual(performRegex(input_text), expected_output)

    def test_remove_special_characters(self):
        input_text = "test@# $% perfomance!"
        expected_output = "test perfomance!"
        self.assertEqual(performRegex(input_text), expected_output)

    def test_remove_extra_spaces(self):
        input_text = "test      Bewerbung  AI  "
        expected_output = "test Bewerbung AI"
        self.assertEqual(performRegex(input_text), expected_output)

    def test_numbers_and_punctuation_remain(self):
        input_text = "12345, test! Bewerbung AI? + -"
        expected_output = "12345, test! Bewerbung AI? + -"
        self.assertEqual(performRegex(input_text), expected_output)

    def test_non_string_input(self):
        input_text = 12345  # An integer
        expected_output = "12345"
        self.assertEqual(performRegex(input_text), expected_output)

    def test_empty_input(self):
        input_text = ""
        expected_output = ""
        self.assertEqual(performRegex(input_text), expected_output)

# Run the tests
if __name__ == '__main__':
    unittest.main()
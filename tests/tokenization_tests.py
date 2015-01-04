import unittest
import tokenizer

__author__ = 'peter'


class TokenizationTests(unittest.TestCase):
    def test_tokenize_single_property(self):
        input = "name = value"
        expected_output = ['name','=','value']
        output = tokenizer.tokenize(input)
        for element_position in range(0,len(output)):
            self.assertTrue(output[element_position] == expected_output[element_position])

    def test_tokenize_multi_propety(self):
        input = "name = {\n\tvalue1 value2\n}"
        expected_output = ['name','=','{','value1','value2','}']
        output = tokenizer.tokenize(input)
        for element_position in range(0,len(output)):
            self.assertTrue(output[element_position] == expected_output[element_position])

    def test_tokenize_compound_property(self):
        input = "condition = or\n\t{\n\t\tfoo = 1\n\t\tfoo = 2\n\t}"
        expected_output = ['condition','=','or','{','foo','=','1','foo','=','2','}']
        output = tokenizer.tokenize(input)
        for element_position in range(0,len(output)):
            self.assertTrue(output[element_position] == expected_output[element_position])

    def test_tokenize_quoted_string(self):
        input = 'name = "value one"'
        expected_output = ['name','=','value one']
        output = tokenizer.tokenize(input)
        for element_position in range(0,len(output)):
            self.assertTrue(output[element_position] == expected_output[element_position])

    def test_tokenize_multiple_keys(self):
        input = 'condition = or\n\t{\n\t\tfoo = 1\n\t\tfoo = "2 many"\n\t}'
        expected_output = ['condition','=','or','{','foo','=','1','foo','=','2 many','}']
        output = tokenizer.tokenize(input)
        for element_position in range(0,len(output)):
            self.assertTrue(output[element_position] == expected_output[element_position])
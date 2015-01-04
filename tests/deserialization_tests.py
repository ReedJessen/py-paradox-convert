import unittest
import deserializer

__author__ = 'peter'


class DeserializationTests(unittest.TestCase):
    def test_deserialize_single_key_value_pair(self):
        input = ['name','=','value']
        expected_output = [{ 'name': 'value' }]
        output = deserializer.deserialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_deserialize_single_key_multi_value(self):
        input = ['name','=','{','first','second', '}']
        expected_output = [{ 'name': ['first', 'second']}]
        output = deserializer.deserialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_deserialize_nested_key(self):
        input = ['name','=','{','sub_name','=','derp','}']
        expected_output = [{ 'name': [{'sub_name': 'derp'}]}]
        output = deserializer.deserialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_deserialize_array_of_kvps(self):
        input = ['name one','=','value one','name two', '=', 'value two']
        expected_output = [{'name one': 'value one'},{'name two':'value two'}]
        output = deserializer.deserialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_deserialize_nested_array(self):
        input = ['name','=','{','sub_name','=','derp','sub_name_2','=','derp2','}']
        expected_output = [{ 'name': [{'sub_name': 'derp'}, {'sub_name_2': 'derp2'}]}]
        output = deserializer.deserialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_deserialize_doubly_nested_key(self):
        input = ['name','=','{','sub_name','=','derp','sub_name_2','=','{','more_nesting','=','a thing','}','}']
        expected_output = [{ 'name': [{'sub_name': 'derp'}, {'sub_name_2': [{'more_nesting':'a thing'}]}]}]
        output = deserializer.deserialize(input)
        self.assertEquals(cmp(expected_output, output), 0)
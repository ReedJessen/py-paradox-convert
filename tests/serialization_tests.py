import unittest
import serializer

__author__ = 'peter'


class SerializationTests(unittest.TestCase):
    def test_serialize_single_key_value_pair(self):
        input = [{ 'name': 'value' }]
        expected_output = "name=value"
        output = serializer.serialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_serialize_single_key_multi_value(self):
        input = [{ 'name': ['first', 'second']}]
        expected_output = 'name={\r\n\tfirst\r\n\tsecond\r\n}'
        output = serializer.serialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_serialize_nested_key(self):
        input = [{ 'name': [{'sub_name': 'derp'}]}]
        expected_output = 'name={\r\n\tsub_name=derp\r\n}'
        output = serializer.serialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_serialize_array_of_kvps(self):
        input = [{'name one': 'value one'},{'name two':'value two'}]
        expected_output = 'name one=value one\r\nname two=value two'
        output = serializer.serialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_serialize_nested_array(self):
        input = [{ 'name': [{'sub_name': 'derp'}, {'sub_name_2': 'derp2'}]}]
        expected_output = 'name={\r\n\tsub_name=derp\r\n\tsub_name_2=derp2\r\n}'
        output = serializer.serialize(input)
        self.assertEquals(cmp(expected_output, output), 0)

    def test_serialize_doubly_nested_key(self):
        input = [{ 'name': [{'sub_name': 'derp'}, {'sub_name_2': [{'more_nesting':'a thing'}]}]}]
        expected_output = 'name={\r\n\tsub_name=derp\r\n\tsub_name_2={\r\n\t\tmore_nesting=a thing\r\n\t}\r\n}'
        output = serializer.serialize(input)
        self.assertEquals(cmp(expected_output, output), 0)
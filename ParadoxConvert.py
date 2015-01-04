from deserializer import deserialize
from serializer import serialize

__author__ = 'peter'


def deserialize_eu4_text_to_object(text):
    return deserialize(text)

def serialize_object_to_eu4_file(node):
    return serialize(node)
py-paradox-convert
==================

Serialize and deserialize Paradox Entertainment's file format! This is a very simple serializer/deserializer that converts back and forth between a python object and plaintext.

Deserialization examples
========================
```python
with open('example.txt','rb') as file:
  print ParadoxConvert.deserialize_eu4_text_to_object(file.read())
```

Serialization examples
======================
```python
with open('example.txt','w+b') as file:
  file.write(ParadoxConvert.serialize_object_to_eu4_file(an_object))
```

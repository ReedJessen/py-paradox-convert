py-paradox-convert
==================

Serialize and deserialize Paradox Entertainment's file format! This is a very simple serializer/deserializer that converts back and forth between a python object and plaintext.

Deserialization examples
========================
```python
with open('example.txt','rb') as file:
  print deserializer.deserialize(file.read())
```

Serialization examples
======================
```python
with open('example.txt','w+b') as file:
  file.write(serializer.serialize(an_object))
```

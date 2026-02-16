# Python - Serialization

## Project Overview

This project explores the fundamental concepts of **serialization and deserialization** in Python. Serialization converts Python objects into a format that can be stored or transmitted, while deserialization restores the object from that format.

The project covers three serialization formats:

- **JSON**
- **Pickle**
- **XML**

Each task demonstrates how data can be transformed between Python objects and persistent storage formats.

---

## Learning Objectives

By completing this project, you will be able to:

- Understand serialization and deserialization
- Work with JSON serialization
- Serialize and deserialize custom classes using pickle
- Convert CSV data to JSON format
- Serialize and deserialize data using XML
- Handle file operations safely with context managers
- Manage exceptions when reading and writing files

---

## Project Structure

python-serialization/
│
├── task_00_basic_serialization.py
├── task_01_pickle.py
├── task_02_csv.py
├── task_03_xml.py
└── README.md

---

## Task 0 – Basic JSON Serialization

**File:** `task_00_basic_serialization.py`

### Objective

- Serialize a Python dictionary into a JSON file
- Deserialize JSON data back into a Python dictionary

### Functions

```python
serialize_and_save_to_file(data, filename)
load_and_deserialize(filename)
```

### Example Output

{'name': 'John Doe', 'age': 30, 'city': 'New York'}

---

## Task 1 – Pickling Custom Classes

**File:** `task_01_pickle.py`

### Objective

 - Create a custom Python class and serialize it using pickle.

**Class:** CustomObject

Attributes:
- name (string)
- age (integer)
- is_student (boolean)

Methods:
- display()
- serialize(filename)
- deserialize(filename) (class method)

### Example Output

Original Object:
Name: John
Age: 25
Is Student: True

Deserialized Object:
Name: John
Age: 25
Is Student: True

---

## Task 2 – Converting CSV to JSON

**File:** `task_02_csv.py`

### Objective

- Read CSV data and convert it to JSON format.

### Function

```python
convert_csv_to_json(filename)
```

### Example JSON Output

[
    {"name": "John", "age": "28", "city": "New York"},
    {"name": "Alice", "age": "24", "city": "Los Angeles"}
]

---

## Task 3 – XML Serialization and Deserialization

**File:** `task_03_xml.py`

### Objective

- Serialize a dictionary to XML
- Deserialize XML back to a Python dictionary

### Functions

```python
serialize_to_xml(dictionary, filename)
deserialize_from_xml(filename)
```

### Example XML Output

<data>
    <name>John</name>
    <age>28</age>
    <city>New York</city>
</data>

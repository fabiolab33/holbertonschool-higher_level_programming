# Python - Input/Output

This project focuses on file handling, JSON serialization and deserialization, command-line arguments, object representation, and algorithmic problem solving in Python.

It explores how Python manages input and output operations, how data can be stored persistently using JSON, and how objects can be converted to and reconstructed from serializable formats.

The final task introduces Pascal’s Triangle to reinforce logical thinking and whiteboard-style problem solving.

---

## Learning Objectives

By completing this project, I understand:

- How to open and close files properly
- How to read a file entirely or line by line
- How to write and append content to files
- How to safely handle files using the `with` statement
- How file cursors work
- What JSON is and why it is useful
- The concepts of serialization and deserialization
- How to convert Python objects to JSON strings
- How to convert JSON strings back to Python objects
- How to save and load Python objects from files
- How to use command-line arguments with `sys.argv`
- How to represent object instances as dictionaries
- How to rebuild objects from serialized data
- How to implement Pascal’s Triangle algorithmically

---

## Project Structure

python-input_output/
│
├── 0-read_file.py
├── 1-write_file.py
├── 2-append_write.py
├── 3-to_json_string.py
├── 4-from_json_string.py
├── 5-save_to_json_file.py
├── 6-load_from_json_file.py
├── 7-add_item.py
├── 8-class_to_json.py
├── 9-student.py
├── 10-student.py
├── 11-student.py
└── 12-pascal_triangle.py

---

## Tasks Description

### 0. Read File
Reads a UTF-8 text file and prints its content to standard output.

### 1. Write to a File
Writes a string to a UTF-8 text file and returns the number of characters written.

### 2. Append to a File
Appends a string to the end of a UTF-8 file and returns the number of characters added.

### 3. To JSON String
Converts a Python object into a JSON string using `json.dumps()`.

### 4. From JSON String to Object
Converts a JSON string back into a Python object using `json.loads()`.

### 5. Save Object to a File
Writes a Python object to a file in JSON format using `json.dump()`.

### 6. Create Object from a JSON File
Loads and returns a Python object from a JSON file using `json.load()`.

### 7. Load, Add, Save
Loads a list from `add_item.json`, adds command-line arguments, and saves the updated list back to the file.

### 8. Class to JSON
Returns the dictionary representation of an object using `__dict__`.

### 9. Student to JSON
Defines a `Student` class with a method that returns its dictionary representation.

### 10. Student to JSON with Filter
Enhances the `Student` class to allow filtering specific attributes when exporting to dictionary format.

### 11. Student to Disk and Reload
Adds a method to update a `Student` instance from a dictionary, simulating deserialization.

### 12. Pascal's Triangle
Implements a function that generates Pascal’s Triangle up to `n` rows.

- Returns an empty list if `n <= 0`
- Time complexity: O(n²)
- No imports allowed

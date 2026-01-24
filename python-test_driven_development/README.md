# Python - Test Driven Development

## Description
This project focuses on Test-Driven Development (TDD) in Python. The main objectives are to understand the importance of testing, learn how to write comprehensive test cases using doctest and unittest, and implement functions that pass all edge cases.

### General
- Why Python programming is awesome
- What's an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

### Testing Concepts
- The importance of writing tests before implementing functionality
- How to use the `doctest` module for interactive testing
- How to use the `unittest` module for comprehensive test suites
- How to validate functions against various edge cases
- How to handle type validation and error messages

### Python Test Cases
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed using: `python3 -m doctest ./tests/*`
- All modules should have documentation: `python3 -c 'print(__import__("my_module").__doc__)'`
- All functions should have documentation: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- Documentation should be real sentences explaining the purpose of the module, class, or method

## Project Tasks

### 0. Integers addition
**File:** `0-add_integer.py`, `tests/0-add_integer.txt`

Write a function that adds 2 integers.
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a TypeError
- `a` and `b` must be first casted to integers if they are float
- Returns an integer: the addition of a and b

**Usage:**
```python
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100.3, -2)
98
```

### 1. Divide a matrix
**File:** `2-matrix_divided.py`, `tests/2-matrix_divided.txt`

Write a function that divides all elements of a matrix.
- Prototype: `def matrix_divided(matrix, div):`
- `matrix` must be a list of lists of integers or floats
- Each row of the matrix must be of the same size
- `div` must be a number (integer or float)
- `div` can't be equal to 0
- All elements of the matrix should be divided by div, rounded to 2 decimal places
- Returns a new matrix

**Usage:**
```python
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
```

### 2. Say my name
**File:** `3-say_my_name.py`, `tests/3-say_my_name.txt`

Write a function that prints `My name is <first name> <last name>`.
- Prototype: `def say_my_name(first_name, last_name=""):`
- `first_name` and `last_name` must be strings
- Raises TypeError with appropriate message if arguments are not strings

**Usage:**
```python
>>> say_my_name = __import__('3-say_my_name').say_my_name
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Bob")
My name is Bob 
```

### 3. Print square
**File:** `4-print_square.py`, `tests/4-print_square.txt`

Write a function that prints a square with the character `#`.
- Prototype: `def print_square(size):`
- `size` is the size length of the square
- `size` must be an integer, otherwise raise TypeError
- If `size` is less than 0, raise ValueError
- If `size` is a float and is less than 0, raise TypeError

**Usage:**
```python
>>> print_square = __import__('4-print_square').print_square
>>> print_square(4)
####
####
####
####
```

### 4. Text indentation
**File:** `5-text_indentation.py`, `tests/5-text_indentation.txt`

Write a function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.
- Prototype: `def text_indentation(text):`
- `text` must be a string, otherwise raise TypeError
- There should be no space at the beginning or at the end of each printed line

**Usage:**
```python
>>> text_indentation = __import__('5-text_indentation').text_indentation
>>> text_indentation("Hello. World? Yes: Good")
Hello.
<BLANKLINE>
World?
<BLANKLINE>
Yes:
<BLANKLINE>
Good
```

### 5. Max integer - Unittest
**File:** `tests/6-max_integer_test.py`

Write unittests for the function `def max_integer(list=[]):`.
- Test file should be inside folder `tests`
- Use the `unittest` module
- Test file should be a Python file (extension: `.py`)
- Execute tests using: `python3 -m unittest tests.6-max_integer_test`
- All tests must be passable by the provided function

**Usage:**
```bash
python3 -m unittest tests.6-max_integer_test
```

## Testing

### Running Doctests
```bash
# Run all doctests
python3 -m doctest ./tests/*

# Run specific test file with verbose output
python3 -m doctest -v ./tests/0-add_integer.txt
```

### Running Unittests
```bash
# Run all unittests
python3 -m unittest tests.6-max_integer_test

# Run with verbose output
python3 -m unittest tests.6-max_integer_test -v
```

### Checking Code Style
```bash
# Check specific file
pycodestyle 0-add_integer.py

# Check all Python files
pycodestyle *.py
```

### Verifying Documentation
```bash
# Check module documentation
python3 -c 'print(__import__("0-add_integer").__doc__)'

# Check function documentation
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
```

## Project Structure
```
python-test_driven_development/
├── README.md
├── 0-add_integer.py
├── 2-matrix_divided.py
├── 3-say_my_name.py
├── 4-print_square.py
├── 5-text_indentation.py
├── 6-max_integer.py
└── tests/
    ├── 0-add_integer.txt
    ├── 2-matrix_divided.txt
    ├── 3-say_my_name.txt
    ├── 4-print_square.txt
    ├── 5-text_indentation.txt
    └── 6-max_integer_test.py
```

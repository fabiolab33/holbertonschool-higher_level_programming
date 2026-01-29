# Python - More Classes and Objects

## Description
This project continues the exploration of **Object-Oriented Programming (OOP)** in Python. It covers more advanced concepts such as class attributes, tracking instances, static methods, class methods, and the lifecycle of an object (initialization and destruction).

## Learning Objectives
By completing these tasks, I have mastered:
*   **Class vs Instance Attributes**: Understanding when to share data between all instances.
*   **Special Methods**: Implementing `__str__` for user-friendly output and `__repr__` for developer-centric representation (recreatable with `eval()`).
*   **Object Lifecycle**: Using the `__del__` destructor to handle instance cleanup.
*   **Static Methods**: Creating utility functions with `@staticmethod` that relate to the class logic but don't need instance data.
*   **Class Methods**: Implementing `@classmethod` as factory methods to create specific object types (e.g., creating a Square from a Rectangle class).
*   **Data Validation**: Centralizing logic within property setters to ensure object integrity.

## Requirements
*   **Environment**: Ubuntu 20.04 LTS
*   **Interpreter**: Python 3.8.5
*   **Coding Style**: [Pycodestyle 2.7.*](https://pycodestyle.pycqa.org)
*   **Documentation**: Comprehensive Google-style docstrings for all modules, classes, and methods.

## Tasks Summary

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Simple rectangle** | `0-rectangle.py` | Basic empty class definition. |
| **1. Real definition** | `1-rectangle.py` | Added private attributes `width` and `height` with property setters. |
| **2. Area and Perimeter** | `2-rectangle.py` | Implemented public methods for area and perimeter calculations. |
| **3. String representation** | `3-rectangle.py` | Added `__str__` to print the rectangle using the `#` character. |
| **4. Eval is magic** | `4-rectangle.py` | Added `__repr__` to allow recreation of instances using `eval()`. |
| **5. Detect deletion** | `5-rectangle.py` | Implemented `__del__` to print a message when an object is destroyed. |
| **6. Instance tracking** | `6-rectangle.py` | Added a class attribute to count active instances. |
| **7. Custom symbol** | `7-rectangle.py` | Added a class attribute to change the character used for printing. |
| **8. Compare rectangles** | `8-rectangle.py` | Added a static method to compare two rectangles by area. |
| **9. Square factory** | `9-rectangle.py` | Added a class method to create a square (Rectangle with equal sides). |

## Usage
Each module can be imported and used to manage rectangle objects dynamically:

```python
Rectangle = __import__('9-rectangle').Rectangle

# Create a square of size 5
my_square = Rectangle.square(5)
print(my_square)
print("Area:", my_square.area())

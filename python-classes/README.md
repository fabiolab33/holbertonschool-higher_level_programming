# Python - Object-Oriented Programming (Classes & Objects)

## Description
This project explores the foundations of **Object-Oriented Programming (OOP)** in Python. The focus is on creating robust classes, implementing data encapsulation, and using Pythonic patterns for attribute management and validation.

## Learning Objectives
Through these tasks, the following concepts were implemented:
*   **Encapsulation**: Using private attributes (with `__`) to hide internal data.
*   **Validation**: Handling `TypeError` and `ValueError` exceptions to ensure data integrity.
*   **Properties**: Implementing `@property` getters and `@setter` methods for controlled attribute access.
*   **Instance Methods**: Creating functionality like area calculation and visual representation of objects.
*   **Code Quality**: Strict adherence to [Pycodestyle](https://pycodestyle.pycqa.org) and comprehensive documentation using docstrings.

## Requirements
*   **Interpreter**: Python 3.8.5 (Ubuntu 20.04 LTS).
*   **Style Guide**: [Pycodestyle 2.7.*](https://pycodestyle.pycqa.org).
*   **Documentation**: All modules, classes, and methods include descriptive docstrings.

## Project Structure

| Task | File | Description |
| :--- | :--- | :--- |
| **0. My first square** | `0-square.py` | Definition of a basic empty class `Square`. |
| **1. Square with size** | `1-square.py` | Introduction of a private instance attribute `size`. |
| **2. Size validation** | `2-square.py` | Added logic to ensure `size` is a positive integer. |
| **3. Area of a square** | `3-square.py` | Implementation of a method to compute the area. |
| **4. Access and update** | `4-square.py` | Transition to Pythonic getters and setters using properties. |
| **5. Printing a square** | `5-square.py` | Added a method to print the square using `#` characters. |
| **6. Coordinates** | `6-square.py` | Expanded the class to handle 2D coordinates for printing. |

## How to Use
Each file is a standalone module. You can import the `Square` class into your own scripts:

```python
Square = __import__('6-square').Square
my_square = Square(3, (2, 1))
my_square.my_print()

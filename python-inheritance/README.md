# Python - Inheritance

## Description
This project focuses on the fundamental concepts of **Inheritance** in Python. The main objective is to understand how classes can inherit attributes and methods from one another, facilitating code reuse, hierarchical organization, and polymorphism. A hierarchy of geometric classes is implemented to demonstrate these concepts in practice.

---

## Learning Objectives
By the end of this project, I am able to explain and apply:
*   **Superclasses and Subclasses**: Definition and use of class hierarchies.
*   **Method Overriding**: How to modify the behavior of an inherited method.
*   **Inspection Functions**: Proper use of `type()`, `isinstance()`, `issubclass()`, and `dir()`.
*   **Exception Handling**: Raising errors to enforce method implementation in base classes.
*   **Use of `super()`**: Invoking constructors and methods from the parent class.
*   **Data Validation**: Centralizing validation logic in a base class to be utilized by its descendants.

---

## Tasks Summary

| Task | File | Description |
| :--- | :--- | :--- |
| **0. Lookup** | `0-lookup.py` | Function that returns the list of available attributes and methods of an object. |
| **1. My list** | `1-my_list.py` | Class that inherits from `list` with a method to print the sorted content. |
| **2. Exact same object** | `2-is_same_class.py` | Validation of exact class identity using `type()`. |
| **3. Same class or inherit** | `3-is_kind_of_class.py` | Validation of class membership or inheritance using `isinstance()`. |
| **4. Only sub class of** | `4-inherits_from.py` | Verification if an object inherits from a class (excluding the class itself). |
| **5. Geometry module** | `5-base_geometry.py` | Creation of an empty base class for geometry. |
| **6. Improve Geometry** | `6-base_geometry.py` | Addition of an `area()` method that raises an "unimplemented" exception. |
| **7. Integer validator** | `7-base_geometry.py` | Implementation of a method to validate positive integers. |
| **8. Rectangle** | `8-rectangle.py` | `Rectangle` class that inherits from `BaseGeometry` and validates dimensions. |
| **9. Full rectangle** | `9-rectangle.py` | Implementation of `area()` and `__str__` for the `Rectangle` class. |
| **10. Square #1** | `10-square.py` | `Square` class that inherits from `Rectangle` using `super().__init__`. |
| **11. Square #2** | `11-square.py` | Complete customization of the string representation (`__str__`) for `Square`. |

---

## Tests
To run the validation tests for this project:
```bash
python3 -m doctest -v ./tests/*.txt

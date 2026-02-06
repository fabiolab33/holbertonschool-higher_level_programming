# Python - Object-Oriented Programming: ABC and Interfaces

## Description
This project focuses on mastering advanced **Object-Oriented Programming (OOP)** concepts in Python. It covers the implementation of **Abstract Base Classes (ABCs)**, formal and informal interfaces (**Duck Typing**), **Multiple Inheritance**, and the use of **Mixins**. The goal is to design modular, reusable, and robust code by enforcing class structures and extending built-in Python functionalities.

## Learning Objectives
*   **Abstract Base Classes:** Use the `abc` module to create blueprints for subclasses.
*   **Interfaces & Duck Typing:** Implement polymorphic functions that rely on object behavior rather than type.
*   **Subclassing Built-ins:** Extend standard classes like `list` and `iterator` to add custom logic.
*   **Multiple Inheritance & MRO:** Understand how Python resolves method calls in complex hierarchies.
*   **Mixins:** Use small, specialized classes to compose behaviors across unrelated classes.

---

## Project Tasks

### 0. Abstract Animal Class
Definition of an abstract base class `Animal` that requires subclasses to implement a `sound()` method.
*   **Key Concept:** Enforcing a specific interface across different animal types (`Dog`, `Cat`).
*   **File:** `task_00_abc.py`

### 1. Shapes, Interfaces, and Duck Typing
Design of a `Shape` interface for geometric figures.
*   **Key Concept:** Using **Duck Typing** in a `shape_info` function to calculate area and perimeter without explicit type checking.
*   **File:** `task_01_duck_typing.py`

### 2. Extending the Python List (VerboseList)
A custom list class that prints a notification every time an item is added or removed.
*   **Key Concept:** Overriding `append`, `extend`, `remove`, and `pop` while maintaining original list functionality via `super()`.
*   **File:** `task_02_verboselist.py`

### 3. CountedIterator - Keeping Track
An iterator wrapper that tracks the number of items successfully iterated.
*   **Key Concept:** Overriding the `__next__` method to increment a counter before returning the next item.
*   **File:** `task_03_countediterator.py`

### 4. Multiple Inheritance (FlyingFish)
Implementation of a `FlyingFish` class that inherits from both `Fish` and `Bird`.
*   **Key Concept:** Exploring **Method Resolution Order (MRO)** and how Python handles overlapping methods in multiple parents.
*   **File:** `task_04_flyingfish.py`

### 5. Mixins (Dragon)
Using `SwimMixin` and `FlyMixin` to grant a `Dragon` class specific abilities.
*   **Key Concept:** Composition over inheritance, allowing for modular behavior without a rigid hierarchy.
*   **File:** `task_05_dragon.py`

---

## Execution
To test any of the tasks, ensure the files are executable and run the corresponding `main` script:

```bash
chmod +x main_01_duck_typing.py
./main_01_duck_typing.py

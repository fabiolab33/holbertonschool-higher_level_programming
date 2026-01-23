# Python - Exceptions

## Project Description

This project focuses on understanding and using **errors and exceptions in Python**.
It covers how to safely handle runtime errors using `try`, `except`, `else`, and `finally`,
as well as how to raise built-in exceptions when needed.

The goal is to write robust Python code that does not crash unexpectedly and properly
handles invalid input or edge cases.

---

## Tasks

### **0. Safe list printing**
Prints a specified number of elements from a list using exception handling.

**File:** `0-safe_print_list.py`

---

### **1. Safe printing of an integers list**
Safely prints an integer using `"{:d}".format()` and returns whether the print was successful.

**File:** `1-safe_print_integer.py`

---

### **2. Print and count integers**
Prints only integer elements from a list up to a given index, skipping invalid types silently.
Raises an exception if the index is out of range.

**File:** `2-safe_print_list_integers.py`

---

### **3. Integers division with debug**
Divides two integers and prints the result inside a `finally` block, even if an error occurs.

**File:** `3-safe_print_division.py`

---

### **4. Divide a list**
Divides elements from two lists index by index while handling:
- wrong types
- division by zero
- out of range access

**File:** `4-list_division.py`

---

### **5. Raise exception**
Raises a `TypeError` intentionally.

**File:** `5-raise_exception.py`

---

### **6. Raise a message**
Raises a `NameError` with a custom message.

**File:** `6-raise_exception_msg.py`

---

## Conclusion

This project strengthens the understanding of Python exception handling and enforces
writing defensive, clean, and readable code. It also highlights how to properly manage
unexpected runtime behavior without relying on external modules or unsafe practices.

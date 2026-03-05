# Python - Object Relational Mapping (ORM) Project

## Project Overview

This project links Python with MySQL databases, combining raw SQL queries and Object Relational Mapping (ORM) using SQLAlchemy. The project is structured into 14 tasks that progressively teach you:

- How to connect to a MySQL database from Python
- How to execute SELECT and INSERT queries using MySQLdb
- How to prevent SQL injection attacks
- How to model MySQL tables as Python classes using SQLAlchemy
- How to query, update, insert, and delete objects using an ORM

All tasks were tested with MySQL 8.0 and Python 3.x.

---

## Tasks

### 0. Select states
- List all states from a database using MySQLdb.
- Sort results by `id`.

### 1. Filter states
- List states with names starting with `'N'`.
- Sort results by `id`.

### 2. Filter states by user input
- List states where the name matches a user-provided argument.
- Vulnerable to SQL injection.

### 3. Safe filter states
- Same as Task 2, but safe from SQL injection using parameterized queries.

### 4. Cities by states
- List all cities with their state names using a single query.
- Sort results by city `id`.

### 5. Filter cities by state
- List all cities of a given state name (argument), safe from SQL injection.
- Results sorted by city `id`.

### 6. First state model
- Create a Python class `State` using SQLAlchemy ORM.
- Maps to the `states` table in MySQL.
- Attributes: `id` (primary key), `name` (max 128 chars).

### 7. All states via SQLAlchemy
- List all State objects from the database using SQLAlchemy.
- Sort by `id`.

### 8. First state
- Print the first State object by `id`.
- If table is empty, print `Nothing`.

### 9. States containing 'a'
- List all State objects containing the letter `'a'`.
- Sort by `id`.

### 10. Get a state
- Print the `id` of the State object matching a given name.
- Print `Not found` if no match exists.
- Safe from SQL injection.

### 11. Add a new state
- Add a new State object `"Louisiana"`.
- Print the new `id`.

### 12. Update a state
- Update the name of the State with `id = 2` to `"New Mexico"`.

### 13. Delete states
- Delete all State objects containing the letter `'a'`.

### 14. Cities in state
- Create a Python class `City` using SQLAlchemy ORM.
- List all cities with their state names.
- Format: `<state name>: (<city id>) <city name>`.

---

## Installation

```bash
# Install Python 3 and MySQL client libraries
sudo apt update
sudo apt install python3-dev libmysqlclient-dev zlib1g-dev mysql-server

# Install Python modules
sudo pip3 install mysqlclient==2.0.3
sudo pip3 install SQLAlchemy==1.4.22
```
# SQL Introduction Project

This project contains 16 tasks designed to practice **MySQL** commands, queries, and database manipulation.

All scripts were tested on **MySQL 8.0** and follow the project rules:

- SQL keywords are in **uppercase**.  
- Each script starts with a **comment describing the task**.  
- All files end with a **newline**.  
- The database name is passed as an argument when required.  

---

## Tasks Overview

### 0. List Databases
List all databases on the MySQL server.  

```bash
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

### 1. Create Database
Create the database `hbtn_0c_0` if it does not exist.

### 2. Delete Database
Delete the database `hbtn_0c_0` if it exists.

### 3. List Tables
List all tables in a given database.

### 4. First Table
Create a table called `first_table` with columns:

- `id` INT
- `name` VARCHAR(256)

### 5. Full Description
Print the full description of `first_table` using `SHOW CREATE TABLE`.

### 6. List All in Table
List all rows of `first_table`.

### 7. First Add
Insert a row into `first_table`:

- `id = 89`
- `name = 'Best School'`

### 8. Count 89
Display the number of records in `first_table` where `id = 89`.

### 9. Full Creation
Create a `table second_table` with columns:
- `id` INT
- `name` VARCHAR(256)
- `score` INT

Insert multiple rows:

| id | name   | score |
|----|--------|-------|
| 1  | John   | 10    |
| 2  | Alex   | 3     |
| 3  | Bob    | 14    |
| 4  | George | 8     |

### 10. List by Best
List all records in `second_table` displaying `score` and `name`, ordered by **score descending**.

### 11. Select the Best
List records in `second_table` where `score >= 10`, ordered by **score descending**.

### 12. Cheating is Bad
Update Bob's score to 10 **without using his id**, only the `name` field.

### 13. Score Too Low
Delete all records in `second_table` where `score <= 5`.

### 14. Average
Compute the average score of all records in `second_table`.

The result column should be named **average**.

### 15. Number by Score
List the number of records for each score in `second_table`.

Columns:
- `score`
- `number` - number of records

Order by `number` descending.

### 16. Say My Name
List all records in `second_table` **excluding rows where `name` is NULL**, showing `score` and `name`, ordered by **score descending**.

## How to Run

```bash
cat <script_name.sql> | mysql -hlocalhost -uroot -p <database_name>
```

Replace `<script_name.sql>` with the SQL file and `<database_name>` when required.
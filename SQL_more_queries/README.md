# SQL More Queries - Holberton School Project

This repository contains SQL scripts that cover advanced queries, user management, table creation, constraints, and joins. The project uses MySQL 8.0 and focuses on relational database management, many-to-many relationships, and query optimization.

All scripts have comments describing their purpose and follow the Holberton School style guidelines: SQL keywords are uppercase, and each file ends with a new line. The database name is passed as an argument when needed.

## Files Overview

### 0. `0-privileges.sql`
Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on `localhost`.

### 1. `1-create_user.sql`
Creates the MySQL user `user_0d_1` with all privileges and password `user_0d_1_pwd`. If the user already exists, the script does not fail.

### 2. `2-create_read_user.sql`
Creates the database `hbtn_0d_2` and the MySQL user `user_0d_2` with only `SELECT` privileges on this database. Password is `user_0d_2_pwd`.

### 3. `3-force_name.sql`
Creates the table `force_name` with columns:
- `id` INT
- `name` VARCHAR(256) NOT NULL  
Fails if inserting without `name` to ensure the `NOT NULL` constraint works.

### 4. `4-never_empty.sql`
Creates the table `id_not_null` with columns:
- `id` INT DEFAULT 1
- `name` VARCHAR(256)

The `id` cannot be null; default value applies when no id is provided.

### 5. `5-unique_id.sql`
Creates the table `unique_id` with columns:
- `id` INT DEFAULT 1 UNIQUE
- `name` VARCHAR(256)

Ensures uniqueness of `id`.

### 6. `6-states.sql`
Creates the database `hbtn_0d_usa` and table `states`:
- `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL
- `name` VARCHAR(256) NOT NULL

### 7. `7-cities.sql`
Creates the table `cities` in `hbtn_0d_usa`:
- `id` INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL
- `state_id` INT NOT NULL, FOREIGN KEY referencing `states(id)`
- `name` VARCHAR(256) NOT NULL

### 8. `8-cities_of_california_subquery.sql`
Lists all cities of California without using `JOIN`, using a subquery to get `state_id`. Results are ordered by `cities.id`.

### 9. `9-cities_by_state_join.sql`
Lists all cities along with their state names using a single `SELECT` with a join. Results ordered by `cities.id`.

### 10. `10-genre_id_by_show.sql`
Lists all shows with at least one genre. Displays:
- `tv_shows.title`
- `tv_show_genres.genre_id`  
Ordered by title and genre_id.

### 11. `11-genre_id_all_shows.sql`
Lists all shows including those without any genre. Shows with no genre display `NULL`. Ordered by title and genre_id.

### 12. `12-no_genre.sql`
Lists all shows **without any genre**. Uses `LEFT JOIN` and filters `NULL` genre_id. Ordered by title and genre_id.

### 13. `13-count_shows_by_genre.sql`
Lists all genres with the number of shows linked. Columns:
- `genre`
- `number_of_shows`  
Only genres with at least one show are shown, ordered by number_of_shows descending.

### 14. `14-my_genres.sql`
Lists all genres of the show `Dexter`. Ordered by genre name.

### 15. `15-comedy_only.sql`
Lists all shows that have the genre `Comedy`. Ordered by show title.

### 16. `16-shows_by_genre.sql`
Lists all shows and their genres. Shows without a genre display `NULL`. Ordered by show title and genre name.

---

## Notes

- All scripts are idempotent where possible (creating users, databases, and tables does not fail if they already exist).  
- Queries include proper ordering and constraints (`NOT NULL`, `UNIQUE`, `PRIMARY KEY`, `FOREIGN KEY`).  
- Many-to-many relationships are handled through join tables (e.g., `tv_show_genres`).  

---

This project demonstrates advanced SQL techniques, including:

- User and privilege management
- Table creation with constraints
- Single and multiple joins
- Subqueries
- Aggregation with GROUP BY
- Handling NULLs with LEFT JOIN
- Ordering query results
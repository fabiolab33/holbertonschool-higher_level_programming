-- List records with a non-null name ordered by score descending
-- This script excludes rows where name is NULL
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
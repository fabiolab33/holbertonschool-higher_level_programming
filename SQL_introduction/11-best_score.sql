-- List records with a score greater than or equal to 10
-- This script displays score and name ordered by score descending
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
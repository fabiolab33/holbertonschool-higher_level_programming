-- List the number of records for each score in second_table
-- This script groups records by score and orders by the count descending
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
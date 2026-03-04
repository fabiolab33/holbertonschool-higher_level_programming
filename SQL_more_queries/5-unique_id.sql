-- Create the table unique_id with id default value 1 and unique constraint
-- Table should not fail if it already exists

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
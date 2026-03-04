-- Create the table force_name with id INT and name VARCHAR(256) NOT NULL
-- Table should not fail if it already exists

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
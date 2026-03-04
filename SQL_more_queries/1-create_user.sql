-- 1-create_user.sql
-- Create the MySQL user 'user_0d_1' with all privileges on localhost
-- Safe: does not fail if user already exists

-- Create user only if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- If user already exists, update password to ensure it's correct
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges globally
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Apply changes immediately
FLUSH PRIVILEGES;
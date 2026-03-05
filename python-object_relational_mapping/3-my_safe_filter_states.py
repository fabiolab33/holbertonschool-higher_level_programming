#!/usr/bin/python3
"""
3-my_safe_filter_states.py: Lists all states from the database
hbtn_0e_0_usa where name matches the user input, safe from SQL injection.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb

def main():
    """Connect to MySQL, filter states by user input safely, and print them sorted by id."""
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cur = db.cursor()

    # Safe query using parameterized statements
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
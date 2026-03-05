#!/usr/bin/python3
"""
2-my_filter_states.py: Lists all states with a name matching the user input
from the database hbtn_0e_0_usa. Results are sorted by states.id.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name>
"""

import sys
import MySQLdb

def main():
    """Connect to MySQL, filter states by user input, and print them sorted by id."""
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

    # SQL query using format() with user input
    query = "SELECT * FROM states WHERE name='{}' ORDER BY id ASC".format(state_name)
    cur.execute(query)

    # Fetch and print results
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
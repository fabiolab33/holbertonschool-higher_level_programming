#!/usr/bin/python3
"""
0-select_states.py: Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

def main():
    """Connects to MySQL and prints all states sorted by id."""
    # Get arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create cursor
    cur = db.cursor()

    # Execute query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
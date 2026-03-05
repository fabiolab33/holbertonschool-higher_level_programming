#!/usr/bin/python3
"""
1-filter_states.py: Lists all states with a name starting with 'N'
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def main():
    """Connects to MySQL and prints states with names starting with 'N', sorted by id."""
    # Get command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor
    cur = db.cursor()

    # Execute query to filter states starting with 'N'
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print each row
    for row in cur.fetchall():
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
#!/usr/bin/python3
"""
5-filter_cities.py: Lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>
Results are sorted by cities.id and safe from SQL injection.
"""

import sys
import MySQLdb

def main():
    """Connect to MySQL, retrieve all cities of a given state, and print them comma-separated."""
    if len(sys.argv) != 5:
        return

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server (native MySQLdb)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # Parameterized query to avoid SQL injection
    cur.execute("""SELECT cities.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (state_name,))

    cities = [row[0] for row in cur.fetchall()]

    # Print results comma-separated, nothing if empty
    print(", ".join(cities), end="")

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
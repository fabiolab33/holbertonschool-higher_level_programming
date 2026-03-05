#!/usr/bin/python3
"""
4-cities_by_state.py: Lists all cities from the database hbtn_0e_4_usa
with their corresponding state name. Results are sorted by cities.id.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

def main():
    """Connect to MySQL and print all cities with state names, sorted by cities.id."""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # JOIN query: cities with their state names, ordered by city id
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               JOIN states ON cities.state_id = states.id
               ORDER BY cities.id ASC"""
    cur.execute(query)

    # Print results
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

if __name__ == "__main__":
    main()
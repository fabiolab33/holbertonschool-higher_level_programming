#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Connects to MySQL and prints the first State object by id."""
    # Get command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object ordered by id
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close session
    session.close()

if __name__ == "__main__":
    main()

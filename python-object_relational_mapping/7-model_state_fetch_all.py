#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Connects to MySQL and lists all State objects sorted by id."""
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

    # Query all State objects, ordered by id
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()

if __name__ == "__main__":
    main()
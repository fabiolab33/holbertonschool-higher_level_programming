#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Connects to MySQL and prints State objects with 'a' in their name, ordered by id."""
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

    # Query states that contain 'a' (case-sensitive), ordered by id
    states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Print results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close session
    session.close()

if __name__ == "__main__":
    main()

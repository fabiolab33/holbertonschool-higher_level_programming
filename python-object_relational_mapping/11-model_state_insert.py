#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa
Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Connects to MySQL, adds Louisiana, and prints its id."""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()  # Save changes to database

    # Print new state's id
    print(new_state.id)

    # Close session
    session.close()

if __name__ == "__main__":
    main()

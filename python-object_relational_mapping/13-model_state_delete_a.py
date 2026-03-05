#!/usr/bin/python3
"""
Deletes all State objects containing the letter 'a' from the database
Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Connects to MySQL and deletes states containing 'a' in their name."""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing 'a' in their name
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each state found
    for state in states_to_delete:
        session.delete(state)

    # Commit changes to the database
    session.commit()

    # Close session
    session.close()

if __name__ == "__main__":
    main()

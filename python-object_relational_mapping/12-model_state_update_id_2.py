#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to 'New Mexico'
Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    """Connects to MySQL and updates the state name."""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the state with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"  # Update the name
        session.commit()  # Save changes

    # Close session
    session.close()

if __name__ == "__main__":
    main()

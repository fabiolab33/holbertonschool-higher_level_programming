#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

def main():
    """Connects to MySQL and prints all cities with their state names."""
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities, order by id
    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        # Access the state's name via the foreign key relationship
        state = session.query(State).filter(State.id == city.state_id).first()
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    main()

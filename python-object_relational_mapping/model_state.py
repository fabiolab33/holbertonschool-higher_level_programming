#!/usr/bin/python3
"""
Model definition of a State and an instance Base for SQLAlchemy ORM
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Create declarative base
Base = declarative_base()

class State(Base):
    """
    State class that maps to the 'states' table in MySQL.

    Attributes:
        id (int): Auto-generated unique primary key, cannot be null
        name (str): Name of the state, max length 128, cannot be null
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
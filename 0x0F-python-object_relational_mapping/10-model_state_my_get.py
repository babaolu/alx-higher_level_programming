#!/usr/bin/python3
"""Queries objects from table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    fname = sys.argv[4].split(sep=";")[0].rstrip("\"")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in (
        session.query(State.id)
        .filter(State.name.in_([fname])).order_by(State.id)
    ):
        print(instance[0])

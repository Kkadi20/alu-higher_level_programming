#!/usr/bin/python3
'''
Deletes all State objects with a name containing the letter a (case-insensitive)
'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
     engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    )
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()
    states = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
    session.close()

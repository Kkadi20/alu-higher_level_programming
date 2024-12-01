#!/usr/bin/python3
'''
Deletes all State objects with a name containing the letter a (case-insensitive).
'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    # Create the engine with provided arguments
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}'
    )
    # Bind the engine to a session
    InstanceSession = sessionmaker(bind=engine)
    session = InstanceSession()

    # Query states where the name contains 'a' (case-insensitive)
    states = session.query(State).filter(State.name.ilike('%a%')).all()

    # Delete the selected states
    for state in states:
        session.delete(state)

    # Commit changes
    session.commit()

    # Close the session
    session.close()

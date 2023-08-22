#!/usr/bin/python3
'''
Script that prints the first `State` object from the database `hbtn_0e_6_usa`
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av

if __name__ == '__main__':
    # Create a database engine
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create a base class for declarative models
    Base.metadata.create_all(engine)

    # create session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # pull all records from the database
    result = session.query(State).first()

    if (result is None):
        # print()
        pass
    else:
        print('{}: {}'.format(result.id, result.name))

    session.close()

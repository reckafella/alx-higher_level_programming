#!/usr/bin/python3
''' Script prints all State objects from the database `hbtn_0e_usa` '''
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
    results = session.query(State).all()

    for row in results:
        res = '{}: {}'.format(row.id, row.name)
        print(res)

    session.close()

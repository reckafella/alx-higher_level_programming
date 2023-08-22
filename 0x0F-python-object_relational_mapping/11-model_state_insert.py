#!/usr/bin/python3
'''
Script that lists all `State` objects that contain the letter `a`\
        from the database `hbtn_0e_6_usa`
'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv as av
from sqlalchemy.sql import text
from sqlalchemy.orm.exc import NoResultFound


if __name__ == '__main__':
    # Create a database engine
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(av[1], av[2], av[3])
    engine = create_engine(db_url, pool_pre_ping=True)

    # Create a base class for declarative models
    Base.metadata.create_all(engine)

    # create session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # insert records into the database
    state_name = 'Louisiana'
    state = State(name=state_name)
    session.add(state)
    session.commit()

    # pull all records from the database
    try:
        result = session.query(State).filter(text("name=:name"))\
            .params(name=state_name).one()
        print('{}'.format(result.id))
    except NoResultFound:
        print('Not Found')

    session.close()

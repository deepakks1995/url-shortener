from .db_config import *

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


def get_session(username=None, password=None, host=None, db_name=None):
    """
    This function establishes a database connection an returns a session
    :param username: username of mysql database
    :param password: password of mysql database
    :param host: host of mysql database
    :param db_name: database name
    :return: a mysql session
    """
    if username is not None:
        MYSQL['username'] = username
    else:
        raise ValueError("User name is mandatory")

    if password is not None:
        MYSQL['password'] = password
    else:
        raise ValueError("Password is mandatory")

    if host is not None:
        MYSQL['host'] = host
    else:
        raise ValueError("Host is mandatory")

    if db_name is not None:
        MYSQL['db_name'] = db_name
    else:
        raise ValueError("Database Name is mandatory")

    try:
        engine = create_engine(
            '{engine}://{username}:{password}@{host}/{db_name}'.format(**MYSQL),
            pool_size=MYSQL["pool_size"],
            echo=MYSQL["debug"]
        )

        session_factory = sessionmaker(bind=engine)
        sess = scoped_session(session_factory)
        return sess

    except Exception as err:
        print(err)
        exit()

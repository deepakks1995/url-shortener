from ..config.config import *

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class SessionMaker:
    @staticmethod
    def get_session():
        """
        This function establishes a database connection an returns a session
        :param username: username of mysql database
        :param password: password of mysql database
        :param host: host of mysql database
        :param db_name: database name
        :return: a mysql session
        """
        if MYSQL['username'] is None:
            raise ValueError("User name is mandatory")

        if MYSQL['password'] is None:
            raise ValueError("Password is mandatory")

        if MYSQL['host'] is None:
            raise ValueError("Host is mandatory")

        if MYSQL['db_name'] is None:
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

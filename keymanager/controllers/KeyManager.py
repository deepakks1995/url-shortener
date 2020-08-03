from ..config.config import *
from ..Utils.RandomKey import RandomKeys
from .DBManager import DBManager
from .SessionMaker import SessionMaker
from ..entities.AvailableKeys import AvailableKeys
import concurrent.futures as future
import threading

from ..entities.UsedKeys import UsedKeys


class KeyManager(object):
    local_cache = None

    def __init__(self):
        """
        Constructor inits the local cache and also add the free keys to db
        """
        self.local_cache = set()
        executer = future.ThreadPoolExecutor(max_workers=2)
        executer.submit(self.add_keys_to_db)
        executer.submit(self.__init_cache)

    def __init_cache(self):
        """
        Inits local cache by generating a new batch of keys and pushing them to Used Keys db
        :return:
        """
        sess = SessionMaker.get_session()
        new_batch = self.__generate_new_batch(sess, True)
        DBManager.insert_batch_into_db([UsedKeys(k) for k in new_batch], sess, False)
        self.local_cache.update(new_batch)

    def get_key(self):
        """
        Pop a random key from the local cache. It also checks whether the local cache is going to be empty or not and if
        it does then it fills the local cache. it also checks whether the db has minimum number of keys in it and if does
        not then it inserts a fresh batch of keys on db
        :return: a random key
        """
        if len(self.local_cache) < MIN_LOCAL_CACHE_SIZE and threading.active_count() < 3:
            executer = future.ThreadPoolExecutor(max_workers=2)
            executer.submit(self._update_cache)

            db_size = DBManager.size(SessionMaker.get_session(), True)
            if db_size < MIN_AVAILABLE_KEYS_DB:
                executer.submit(self.add_keys_to_db)

        while len(self.local_cache) == 0:
            pass
        return self.local_cache.pop()

    def _update_cache(self):
        """
        Fnction used to update the local cache.
        :return:
        """
        while len(self.local_cache) < LOCAL_CACHE_SIZE:
            sess = SessionMaker.get_session()
            batch = DBManager.fetch_keys(LOCAL_CACHE_SIZE, sess)

            if len(batch) != 0:
                self.local_cache.update(batch)

    def __generate_new_batch(self, sess, close_session):
        """
        Generates a new batch of random keys and gets them verified whether they have been used before or not
        :param sess: SqlAlchemy Session
        :param close_session: boolean flag whether to close the session after insertion or not
        :return:
        """
        batch = RandomKeys.get_random_key_set(INSERT_BATCH_SIZE, 8)
        verified_batch = DBManager.verify_batch_from_db(batch, sess, close_session)
        return verified_batch

    def add_keys_to_db(self):
        """
        Adds keys to available_keys table until it reaches it capacity i.e. MAX_AVAILABLE_KEYS_DB
        :return:
        """
        db_size = DBManager.size(SessionMaker.get_session(), True)

        if db_size >= MAX_AVAILABLE_KEYS_DB:
            return None

        sess = SessionMaker.get_session()
        while db_size < MAX_AVAILABLE_KEYS_DB:
            batch = self.__generate_new_batch(sess, False)

            if batch is not None and len(batch) != 0:
                DBManager.insert_batch_into_db([AvailableKeys(k) for k in batch], sess, False)
                db_size = db_size + len(batch)

        sess.close()

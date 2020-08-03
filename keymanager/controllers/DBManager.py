from sqlalchemy.exc import IntegrityError

from ..entities.AvailableKeys import AvailableKeys
from ..entities.UsedKeys import UsedKeys


class DBManager:
    @staticmethod
    def insert_batch_into_db(batch, sess, close_session=True):
        """
        Insert bulk objects into database
        :param batch: batch to be inserted
        :param sess: SqlAlchemy Session
        :param close_session: boolean flag whether to close the session after insertion or not
        :return:
        """
        if len(batch) == 0:
            sess.close()
            return None

        try:
            sess.bulk_save_objects(batch)
            sess.commit()
        except IntegrityError:
            sess.rollback()
        except Exception as E:
            sess.rollback()
        finally:
            if close_session:
                sess.close()

    @staticmethod
    def verify_batch_from_db(batch, sess, close_session=True):
        """
        Verifies whether passed is not present in the available_keys and used_keys table
        :param batch: batch to be verified
        :param sess: SqlAlchemy Session
        :param close_session: boolean flag whether to close the session after insertion or not
        :return: batch containing only keys not present in both the tables
        """
        try:
            query1 = sess.query(AvailableKeys).filter(AvailableKeys.keys.in_(list(batch))).all()
            query2 = sess.query(UsedKeys).filter(UsedKeys.keys.in_(list(batch))).all()

            not_allowed = set(k.keys for k in query1 + query2)
            return batch - not_allowed

        except IntegrityError:
            sess.rollback()
        except Exception as e:
            sess.rollback()
        finally:
            if close_session:
                sess.close()

    @staticmethod
    def fetch_keys(size, sess, close_session=True):
        """
        Fetches a batch of keys from available_keys and inserts them back to used_keys and then removes the fetched
        keys from available_keys
        :param size: Size of batch to be fetched
        :param sess: SqlAlchemy Session
        :param close_session: boolean flag whether to close the session after insertion or not
        :return: A new Batch of available keys
        """
        try:
            available_keys = sess.query(AvailableKeys).limit(size).all()
            used_keys = []
            for keys in available_keys:
                sess.delete(keys)
                used_keys.append(UsedKeys(keys.keys))
            sess.commit()

            DBManager.insert_batch_into_db(used_keys, sess)
            return [k.keys for k in available_keys]

        except IntegrityError:
            sess.rollback()
        except Exception as E:
            sess.rollback()
        finally:
            if close_session:
                sess.close()

    @staticmethod
    def size(sess, close_session=True):
        """
        Returns the size of Available Keys table
        :param sess: SqlAlchemy Session
        :param close_session: boolean flag whether to close the session after insertion or not
        :return: number of rows
        """
        try:
            rows = sess.query(AvailableKeys).count()
            return rows
        except IntegrityError:
            sess.rollback()
        except Exception as E:
            sess.rollback()
        finally:
            if close_session:
                sess.close()
from shortener.Utils import HashGenerator
from .entities.url import URL
from .Utils.UniqueKeys import UniqueKeys
import datetime


def __create_hash(url):
    """
    function to create a random hash out of the url passed
    :param url: long url to be processed
    :return: tinyurl
    """
    time_stamp = datetime.datetime.now().timestamp()
    hash = HashGenerator().get_hex(url + str(time_stamp))
    unique_key = UniqueKeys().get_unique_chars(hash)
    return unique_key


def __add_to_sess(sess, url):
    """
    adds an entry to mysql session
    :param sess: mysql session
    :param url: long url to store in db
    :return:
    """
    url_table = URL(__create_hash(url), url)
    sess.add(url_table)
    return url_table.custom


def shorten(sess, url):
    """
    Function used to shorten a single long url
    :param sess: mysql session
    :param url: long url to store in db
    :return:
    """
    try:
        tiny_url = __add_to_sess(sess, url)
        sess.commit()
        return tiny_url

    except Exception as E:
        print(E)
        sess.rollback()


def get_original_url(sess, custom):
    """
    Function used to retrieve a long url given a tiny url is passed
    :param sess: mysql session
    :param custom: tiny url
    :return: long url if available
    """
    try:

        url = sess.query(URL).get(custom)
        if url:
            return url.original

    except Exception as E:
        print(E)


def shorten_from_file(sess, file_path):
    """
    Function to shorten a long urls from a file
    :param sess: mysql session
    :param file_path: file path to be preocessed
    :return: list of tiny urls
    """
    result = []
    with open(file_path, "r") as f:
        line = f.readline()
        while line:
            result.append(shorten(sess, line))
            line = f.readline()
    return result
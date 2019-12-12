import unittest

from alchemy_mock.mocking import AlchemyMagicMock

import shortener


class TestShortener(unittest.TestCase):

    def test_unique_keys(self):
        """
        Test to check uniqueness of two different url passed
        :return:
        """
        sess = AlchemyMagicMock()
        tiny_url_1 = shortener.shorten(sess, "https://timesofindia.indiatimes.com/defaultinterstitial.cms")
        tiny_url_2 = shortener.shorten(sess, "https://indiatoday.in")
        self.assertNotEqual(tiny_url_1, tiny_url_2)

    def test_unique_keys_for_same_url(self):
        """
        Test to check uniqueness of keys of two same url passed
        :return:
        """
        sess = AlchemyMagicMock()
        tiny_url_1 = shortener.shorten(sess, "https://timesofindia.indiatimes.com/defaultinterstitial.cms")
        tiny_url_2 = shortener.shorten(sess, "https://timesofindia.indiatimes.com/defaultinterstitial.cms")
        self.assertNotEqual(tiny_url_1, tiny_url_2)

    def test_unique_keys_for_files(self):
        """
        Test to check uniqueness of keys from a file
        :return:
        """
        sess = AlchemyMagicMock()
        result = shortener.shorten_from_file(sess, "./shortener/data/input.txt")

        unique_keys = set()
        for url in result:
            self.assertFalse(url in unique_keys, "Collision occurred")
            unique_keys.add(url)

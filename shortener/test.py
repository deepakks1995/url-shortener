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
        self.assertNotEqual(tiny_url_1, tiny_url_2, "Collision occurred")

    def test_unique_keys_for_same_url(self):
        """
        Test to check uniqueness of keys of two same url passed
        :return:
        """
        sess = AlchemyMagicMock()
        tiny_url_1 = shortener.shorten(sess, "https://timesofindia.indiatimes.com/defaultinterstitial.cms")
        tiny_url_2 = shortener.shorten(sess, "https://timesofindia.indiatimes.com/defaultinterstitial.cms")
        self.assertNotEqual(tiny_url_1, tiny_url_2, "Collision occurred")

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

    def test_length_test(self):
        """
        Test to check the length of tiny url
        :return:
        """
        sess = AlchemyMagicMock()
        tiny_url = shortener.shorten(sess, "https://timesofindia.indiatimes.com/defaultinterstitial.cms")

        self.assertEqual(len(tiny_url), 8, "Tiny Url length is not 8")

    def test_invalid_url_test(self):
        """
        Test to check whether the program responds to invalid urls
        :return:
        """
        sess = AlchemyMagicMock()
        tiny_url = shortener.shorten(sess, "www.abcdedgskfjlkd.com")
        self.assertEqual("Invalid Url", tiny_url, "Invalid Url is not handled properly")

    def test_valid_url_test(self):
        """
        Test to check whether the program handles valid urls
        :return:
        """
        sess = AlchemyMagicMock()
        tiny_url = shortener.shorten(sess, "https://www.abcdedgskfjlkd.com")
        self.assertNotEqual("Invalid Url", tiny_url, "Valid Url is not handled properly")

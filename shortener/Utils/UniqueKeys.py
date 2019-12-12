import random
import base64


class UniqueKeys:
    length = 0

    def __init__(self, len=8):
        self.length = len

    def get_unique_chars(self, url):
        """
        This functions converts the hash to base64 and then picks random chars out of it
        :param url: url to be processed
        :return:
        """
        counter = 0
        encoded = base64.b64encode(url.encode("utf-8")).decode("utf-8")
        result = ""

        while len(result) < self.length:
            counter += random.randrange(0, 1000)
            counter %= len(encoded)
            result += str(encoded[counter])

        return result

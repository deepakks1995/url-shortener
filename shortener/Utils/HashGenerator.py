import hashlib


class HashGenerator():

    def get_hash(self, key):
        """
        Generates a hash out of a key
        :param key:
        :return:
        """
        return hashlib.md5(key.encode())

    def get_hex(self, key):
        """
        Get a hex output of a hash
        :param key: key to be hashed
        :return:
        """
        return self.get_hash(key).hexdigest()

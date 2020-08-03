import random
import string


class RandomKeys:

    @staticmethod
    def get_random_key(length):
        """
        Generates a random key of certain length
        :param length: length of key to be generated
        :return: random key
        """
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join((random.choice(letters_and_digits) for i in range(length)))

    @staticmethod
    def get_random_key_set(size, length):
        """
        Generates a new batch of random keys of certain size
        :param size: size of batch to be generated
        :param length: length of key to be generated
        :return: batch of random keys
        """
        result = set()

        while len(result) < size:
            result.add(RandomKeys.get_random_key(length))

        return result


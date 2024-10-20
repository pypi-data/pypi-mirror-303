__all__ = ("random_string", "random_hex_string")

import binascii
import os
import string
import random


chars = string.ascii_letters + string.digits


def random_string(length: int):
    """Generate a random string

    Args:
        length (``int``):
            The length of the string
    """

    return "".join(random.choices(chars, k=length))


def random_hex_string(length):
    """Generate a random hex string

    Args:
        length (``int``):
            The length of the string (in bytes)
    """

    return binascii.hexlify(os.urandom(length)).decode()

import hashlib
import json
from urllib.parse import urljoin

import requests
from rest_framework.status import HTTP_200_OK



import requests


def create_hash_from_dict(data):
    """
    Create MD5 hash of dictionary.

    :param data: Dict with data.

    :return: String hash.
    """
    generator = hashlib.md5()
    encoded = json.dumps(data, sort_keys=True).encode()
    generator.update(encoded)
    return generator.hexdigest()

print(create_hash_from_dict("ds"))


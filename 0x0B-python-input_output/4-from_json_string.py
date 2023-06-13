#!/usr/bin/python3

"""  Module returns an object\
    (Python data structure) represented by a JSON string """
import json


def from_json_string(my_str):
    """
    Return an object from JSON string

    Args:
        my_str (str): an object
    """
    return json.loads(my_str)

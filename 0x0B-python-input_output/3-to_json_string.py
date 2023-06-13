#!/usr/bin/python3

import json

"""  a function that returns the JSON representation of an object (string) """


def to_json_string(my_obj):
    """
    Return JSON representation of an object

    Args:
        my_obj (obj): an object
    """
    return json.dumps(my_obj)

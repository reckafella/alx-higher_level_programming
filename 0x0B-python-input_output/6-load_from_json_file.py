#!/usr/bin/python3

""" Module creates an Object from a json file """
import json


def load_from_json_file(filename):
    """ Create an Object from a .json file """

    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)

#!/usr/bin/python3

""" Module contains the Base class that is imported by other classes """
import json
from models.rectangle import Rectangle
from models.square import Square


class Base:
    """Base class

    Attributes:
        id (int): integer value
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor used to initialize each object """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return '{}'.format("\"[]\"")
        else:
            return json.dumps(list_dictionaries)

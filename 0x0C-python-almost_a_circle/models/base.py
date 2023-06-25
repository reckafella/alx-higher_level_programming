#!/usr/bin/python3

""" Module contains the Base class that is imported by other classes """
import json


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
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        file_name = '{}.json'.format(cls.__name__)

        with open(file_name, 'w', encoding='utf-8') as file:
            if list_objs is None:
                file.write()
            else:
                data = []

                for obj in list_objs:
                    data.append(obj.to_dictionary())

                file.write(Base.to_json_string(data))

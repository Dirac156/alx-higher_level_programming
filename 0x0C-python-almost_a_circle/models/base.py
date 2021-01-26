#!/usr/bin/python3
"""The base class  file"""
import json


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """list to json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

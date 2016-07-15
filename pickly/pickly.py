# -*- coding: utf-8 -*-

import json


class AttributeNotFoundException(Exception):

    """
    Exception raised when an attribute isn't found in the json data
    """

    def __init__(self, message):
        super(AttributeNotFoundException, self).__init__(message)


class Pickly(object):

    def __init__(self, json_data):
        if isinstance(json_data, dict) or isinstance(json_data, list):
            self.json = json_data

        if isinstance(json_data, str) or isinstance(json_data, unicode):
            self.json = json.loads(json_data)

    def __getattr__(self, attr):
        if attr not in self.json:
            raise AttributeNotFoundException("{0} doesn't exist".format(attr))

        obj = self.json[attr]
        if isinstance(obj, dict) or isinstance(obj, list):
            return Pickly(obj)

        return obj

    def __getitem__(self, index):
        if not isinstance(self.json, list):
            raise TypeError("Element doesn't support indexing")

        list_size = len(self.json)
        if list_size <= index:
            raise IndexError("Only {0} elements in the list".format(list_size))

        obj_element = self.json[index]
        if isinstance(obj_element, dict):
            return Pickly(obj_element)

        return obj_element

    def __repr__(self):
        return json.dumps(self.json)

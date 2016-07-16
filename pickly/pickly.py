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
            self._json = json_data

        if isinstance(json_data, str) or isinstance(json_data, unicode):
            self._json = json.loads(json_data)

    def __getattr__(self, attr):
        if attr not in self._json:
            raise AttributeNotFoundException("{0} doesn't exist".format(attr))

        obj = self._json[attr]
        if isinstance(obj, dict) or isinstance(obj, list):
            return Pickly(obj)

        return obj

    def __getitem__(self, index):
        if not isinstance(self._json, list):
            raise TypeError("Element doesn't support indexing")

        list_size = len(self._json)
        if list_size <= index:
            raise IndexError("Only {0} elements in the list".format(list_size))

        obj_element = self._json[index]
        if isinstance(obj_element, dict):
            return Pickly(obj_element)

        return obj_element

    def attrs(self):
        """ Returns a list of all accessible attributes within an object """
        if isinstance(self._json, dict):
            return self._json.keys()

    def __repr__(self):
        return json.dumps(self._json)

import json


class AttributeNotFoundException(Exception):

    """
    Exception raised when an attribute isn't found in the json data
    """
    pass


class Pickly(object):

    def __init__(self, json_data):
        if isinstance(json_data, dict) or isinstance(json_data, list):
            self.json = json_data

        if isinstance(json_data, str) or isinstance(json_data, unicode):
            self.json = json.loads(json_data)

    def __getattr__(self, attr):
        if attr not in self.json:
            raise AttributeNotFoundException()

        obj = self.json[attr]

        if isinstance(obj, dict) or isinstance(obj, list):
            return Pickly(obj)

        return obj

    def __getitem__(self, index):
        if not isinstance(self.json, list):
            raise TypeError("Element not of type list")

        list_size = len(self.json)
        if list_size <= index:
            raise IndexError("Only {0} elements in the list".format(list_size))

        element = self.json[index]
        if isinstance(element, dict):
            return Pickly(element)

        return obj

    def __repr__(self):
        return json.dumps(self.json)

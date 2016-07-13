import json


class AttributeNotFoundException(Exception):

    """
    Exception raised when an attribute isn't found in the json data
    """
    pass


class Pickly(object):

    def __init__(self, json_data):
        if isinstance(json_data, dict):
            self.json = json_data

        if isinstance(json_data, str):
            self.json = json.loads(json_data)

    def __getattr__(self, attr):
        if attr not in self.json:
            raise AttributeNotFoundException()

        obj = self.json[attr]

        if isinstance(obj, dict):
            return Pickly(obj)

        return obj

    def __repr__(self):
        return json.dumps(self.json)

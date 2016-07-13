from pickly import Pickly
from pickly.pickly import AttributeNotFoundException

import unittest


class TestPickly(unittest.TestCase):

    def test_invalid_json(self):
        json_str = "Invalid JSON"

        with self.assertRaises(ValueError):
            Pickly(json_str)

    def test_invalid_json_format(self):
        json_str = '''
        {
            name: 'Pickly',
            value: {
        }
        '''

        with self.assertRaises(ValueError):
            Pickly(json_str)

    def test_nonexistant_attribute(self):
        json_str = '''
        {
            "countries": {
                "Pakistan": "Islamabad",
                "USA": "Washington"
            }
        }
        '''

        obj = Pickly(json_str)
        with self.assertRaises(AttributeNotFoundException):
            obj.foo

    def test_chained_objects(self):
        json_str = '''
        {
            "countries": {
                "Pakistan": "Islamabad",
                "USA": "Washington"
            }
        }
        '''

        obj = Pickly(json_str)
        self.assertEquals(obj.countries.Pakistan, "Islamabad")
        self.assertEquals(obj.countries.USA, "Washington")

    def test_init_from_dict(self):
        json_dict = {'countries': {'Pakistan': 'Islamabad'}}
        obj = Pickly(json_dict)
        self.assertEquals(obj.countries.Pakistan, "Islamabad")


if __name__ == '__main__':
    unittest.main()

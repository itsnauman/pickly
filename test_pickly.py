# -*- coding: utf-8 -*-

from pickly import Pickly
from pickly.pickly import AttributeNotFoundException

import unittest


class TestPickly(unittest.TestCase):

    def setUp(self):
        self.valid_json = '''
        {
            "countries": {
                "Pakistan": "Islamabad",
                "USA": "Washington"
            }
        }
        '''

        self.valid_json_with_list = '''
        [
            {
                "countries": {
                    "Pakistan": "Islamabad",
                    "USA": "Washington"
                }
            }
        ]
        '''

        self.json_with_dict_nesting = '''
        [
            {
                "countries": [
                    {
                        "Pakistan": "Islamabad"
                    },
                    {
                        "USA": "Washington"
                    }
                ]
            }
        ]
        '''

        self.readme_example_json = '''
        {
            "friends": [
              {
                "id": 0,
                "name": "Greer Bentley"
              }
            ]
        }
        '''

    def test_invalid_json(self):
        json = "Invalid JSON"

        with self.assertRaises(ValueError):
            Pickly(json)

    def test_invalid_json_format(self):
        json = '''
        {
            name: "Pickly",
            value: {
        }
        '''

        with self.assertRaises(ValueError):
            Pickly(json)

    def test_nonexistant_attribute(self):
        obj = Pickly(self.valid_json)
        with self.assertRaises(AttributeNotFoundException):
            obj.foo

    def test_invalid_index_access(self):
        with self.assertRaises(TypeError):
            Pickly(self.valid_json)[0]

    def test_out_of_bound_index(self):
        obj = Pickly(self.valid_json_with_list)

        with self.assertRaises(IndexError):
            obj[1]  # At length of list

        with self.assertRaises(IndexError):
            obj[2]  # Out of list length

    def test_type_error(self):
        obj = Pickly(self.valid_json_with_list)

        with self.assertRaises(TypeError):
            obj[0].countries[0]

    def test_multiple_indexed_nesting(self):
        obj = Pickly(self.json_with_dict_nesting)

        self.assertTrue(iter(obj))
        self.assertIsInstance(obj[0], Pickly)
        self.assertIsInstance(obj[0].countries[0], Pickly)
        self.assertEqual(obj[0].countries[0].Pakistan, "Islamabad")

    def test_indexing(self):
        obj = Pickly(self.valid_json_with_list)
        self.assertEqual(obj[0].countries.Pakistan, "Islamabad")

    def test_nested_obj_in_list(self):
        obj = Pickly(self.json_with_dict_nesting)

        self.assertIsInstance(obj[0].countries[0], Pickly)
        self.assertEqual(obj[0].countries[1].USA, "Washington")

    def test_chained_objects(self):
        obj = Pickly(self.valid_json)

        self.assertEquals(obj.countries.Pakistan, "Islamabad")
        self.assertEquals(obj.countries.USA, "Washington")

    def test_init_from_dict(self):
        json_dict = {'countries': {'Pakistan': 'Islamabad'}}
        obj = Pickly(json_dict)
        self.assertEquals(obj.countries.Pakistan, "Islamabad")

    def test_no_obj_in_list(self):
        json = '''
        {
            "countries": [
                "Pakistan",
                "USA"
            ]
        }
        '''
        obj = Pickly(json)

        self.assertTrue(iter(obj.countries))
        self.assertEqual(obj.countries[0], "Pakistan")

    def test_repr(self):
        obj = Pickly(self.readme_example_json)

        self.assertIsInstance(repr(obj.friends), str)

    def test_get_attributes(self):
        obj = Pickly(self.readme_example_json)

        self.assertIsNone(obj.friends.attrs())
        self.assertIsNotNone(obj.friends[0].attrs())


if __name__ == '__main__':
    unittest.main()

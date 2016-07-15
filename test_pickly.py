# -*- coding: utf-8 -*-

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
            name: "Pickly",
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

    def test_invalid_index_access(self):
        json_str = '''
        {
            "countries": {
                "Pakistan": "Islamabad",
                "USA": "Washington"
            }
        }
        '''

        with self.assertRaises(TypeError):
            Pickly(json_str)[0]

    def test_out_of_bound_index(self):
        json_str = '''
        [
            {
                "countries": {
                    "Pakistan": "Islamabad",
                    "USA": "Washington"
                }
            }
        ]
        '''
        obj = Pickly(json_str)

        with self.assertRaises(IndexError):
            obj[1]  # At length of list

        with self.assertRaises(IndexError):
            obj[2]  # Out of list length

    def test_invalid_param_type(self):


    def test_multiple_indexed_nesting(self):
        json_str = '''
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
        obj = Pickly(json_str)

        self.assertTrue(iter(obj))
        self.assertIsInstance(obj[0], Pickly)
        self.assertIsInstance(obj[0].countries[0], Pickly)
        self.assertEqual(obj[0].countries[0].Pakistan, "Islamabad")

    def test_indexing(self):
        json_str = '''
        [
            {
                "countries": {
                    "Pakistan": "Islamabad",
                    "USA": "Washington"
                }
            }
        ]
        '''
        obj = Pickly(json_str)

        self.assertEqual(obj[0].countries.Pakistan, "Islamabad")

    def test_nested_obj_in_list(self):
        json_str = '''
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
        '''
        obj = Pickly(json_str)

        self.assertIsInstance(obj.countries[0], Pickly)
        self.assertEqual(obj.countries[1].USA, "Washington")

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

    def test_no_obj_in_list(self):
        json_str = '''
        {
            "countries": [
                "Pakistan",
                "USA"
            ]
        }
        '''
        obj = Pickly(json_str)

        self.assertTrue(iter(obj.countries))
        self.assertEqual(obj.countries[0], "Pakistan")

    def test_readme_example(self):
        json = '''
            [
              {
                "name": "Newman Gates",
                "tags": [
                  "sunt",
                  "cillum"
                ],
                "friends": [
                  {
                    "id": 0,
                    "name": "Greer Bentley"
                  },
                  {
                    "id": 1,
                    "name": "Ebony Montgomery"
                  }
                ]
              }
            ]
        '''
        obj = Pickly(json)

        self.assertEqual(obj[0].name, "Newman Gates")
        self.assertTrue(iter(obj[0].friends))

if __name__ == '__main__':
    unittest.main()

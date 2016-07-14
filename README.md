# Pickly :cactus:
[![Build Status](https://travis-ci.org/itsnauman/pickly.svg?branch=master)](https://travis-ci.org/itsnauman/pickly)

`Pickly` is a tiny library for `JSON` object mapping in `Python`. It you allows to access `JSON` attributes like plain old objects (just like in `Javascript`) rather than dealing with dictionaries (eww!)

## Usage
```python
from pickly import Pickly

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
# Woallah, you are ready! 🎉🍰
obj = Pickly(json)

obj[0].name # Newman Gates

# Iterate through lists
for item in obj[0].friends:
    item.name
```
### Using Pickly with Requests
```python
from pickly import Pickly
import requests

res = requests.get('http://jsonplaceholder.typicode.com/posts')
obj = Pickly(res.text) # You are ready to roll 🔥

for item in obj:
    item.title
```

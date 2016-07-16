# Pickly :cactus:
[![Build Status](https://travis-ci.org/itsnauman/pickly.svg?branch=master)](https://travis-ci.org/itsnauman/pickly)
[![codecov](https://codecov.io/gh/itsnauman/pickly/branch/master/graph/badge.svg)](https://codecov.io/gh/itsnauman/pickly)

`Pickly` is a tiny library for `JSON` object mapping in `Python`. It you allows to access `JSON` attributes like plain old objects just like in `Javascript`. There is no need to deal with dictionaries anymore 🎉

## Installation 
The recommended installation method is pip:
```
$ pip install pickly 
```

## Usage
```python
from pickly import Pickly

json = '''
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
'''
# Woallah, you are ready! 🎉🍰
obj = Pickly(json)

# Print an object to see what's inside
print obj.friends # [{"id": 0, "name": "Greer Bentley"}, {"id": 1, "name": "Ebony Montgomery"}]

print obj.tags[0] # sunt

obj.name # Newman Gates

# Iterate through lists
for item in obj.friends:
    item.name
```
### 👉 Using Pickly with Requests
```python
from pickly import Pickly
import requests

res = requests.get('http://jsonplaceholder.typicode.com/posts')
obj = Pickly(res.text) # You are ready to roll 🔥

for item in obj:
    item.title
```

### 👉 Using Pickly with a JSON file
```python
from pickly import Pickly

with open('file.json', 'r') as fp:
    obj = Pickly(fp.text())

obj.foo.name
```

## Thank You 😀
Thanks for checking this library out! I hope you find it useful.

There's always room for improvement. Feel free to open an issue so we can make Pickly better!

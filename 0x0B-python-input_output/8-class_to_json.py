#!/usr/bin/python3
"""Function returns the dictionary description
with simple data structure
"""

import json


def class_to_json(obj):
    """Return description
    with simple data structure
    """
    data = json.dumps(obj, default=lambda o: o.__dict__)
    return json.loads(data)

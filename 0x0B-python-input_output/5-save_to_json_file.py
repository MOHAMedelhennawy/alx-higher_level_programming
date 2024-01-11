#!/usr/bin/python3
"""Function to write an obj to a text file
"""

import json


def save_to_json_file(my_obj, filename):
    """Write an obj to a text file, using JSON

    Args:
        my_obj: The obj that will be stored in file
        filename: The name of file that will store in
    """

    with open(filename, "w") as file_obj:
        json.dump(my_obj, file_obj)

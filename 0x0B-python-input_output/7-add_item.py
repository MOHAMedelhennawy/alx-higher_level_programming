#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    my_list = sys.argv
    file_name = "add_item.json"
    my_list.pop(0)

    with open(file_name) as file_obj:
        size = len(file_obj.read())

    if size == 0:
        save_to_json_file([], file_name)

    else:
        data = load_from_json_file(file_name)
        save_to_json_file(data + my_list, file_name)

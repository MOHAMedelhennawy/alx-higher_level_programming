#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


    file_name = "add_item.json"
    try:
        items = load_from_json_file(file_name)
    except:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, file_name)

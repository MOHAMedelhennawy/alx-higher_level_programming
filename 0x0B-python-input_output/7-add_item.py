#!/usr/bin/python3
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = sys.argv
file_name = "add_item.json"
my_list.pop(0)


try:
    load_from_json_file(file_name)
except:
    save_to_json_file([], file_name)
else:
    data = load_from_json_file(file_name)
    save_to_json_file(data + my_list, file_name)

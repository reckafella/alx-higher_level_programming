#!/usr/bin/python3

""" Module contains a script that adds arguments to a Python list and then
saves them to a file
"""

import sys
file_loader = __import__("6-load_from_json_file").load_from_json_file
file_saver = __import__("5-save_to_json_file").save_to_json_file

filename = "add_item.json"

try:
    json_list = file_loader(filename)
except FileNotFoundError:
    json_list = []
    file_saver(json_list, filename)
else:
    json_list.extend(sys.argv[1:])
    file_saver(json_list, filename)

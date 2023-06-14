#!/usr/bin/python3

""" Module contains a script that adds arguments to a Python list and then
saves them to a file
"""

import sys
file_loader = __import__("6-load_from_json_file").load_from_json_file
file_saver = __import__("5-save_to_json_file").save_to_json_file

filename = "add_item.json"
if __name__ == "__main__":
    num_args = len(sys.argv)

    arg_list = []

    try:
        json_list = list(file_loader(filename))
    except FileNotFoundError:
        file_saver(arg_list, filename)
    else:
        for arg in range(1, num_args):
            arg_list.append(sys.argv[arg])
        json_list = (json_list) + arg_list
        file_saver(json_list, filename)

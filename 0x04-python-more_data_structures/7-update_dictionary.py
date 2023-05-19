#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    new_dict = a_dictionary

    for i in sorted(new_dict.keys()):
        if (i in new_dict.keys() and i == key):
            new_dict.update({key : value})
        else:
            new_dict[key] = value

    return (new_dict)

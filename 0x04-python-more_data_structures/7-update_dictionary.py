#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for i in sorted(a_dictionary.keys()):
        if (i == key):
            a_dictionary.update({key:value})
        else:
            a_dictionary[key] = value
    return (a_dictionary)

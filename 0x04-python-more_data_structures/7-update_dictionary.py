#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    for i in sorted(a_dictionary.keys()):
        a_dictionary[key] = value
    return (a_dictionary)

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific
    position without modifying the original list
    """
    list_len = len(my_list)
    new_list = []

    if ((idx < 0) or (idx >= list_len)):
        new_list = my_list[:]
        return new_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return new_list

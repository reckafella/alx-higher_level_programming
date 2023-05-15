#!/usr/bin/python3
def element_at(my_list, idx):
    '''
    Retrieve an element from a list
    '''
    num_elements = len(my_list)

    if (idx < 0):
        return None
    if (idx >= num_elements):
        return None
    return (my_list[idx])

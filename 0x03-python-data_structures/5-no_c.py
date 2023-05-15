#!/usr/bin/python3
def no_c(my_string):
    '''
    Remove all characters c and C from a string
    '''

    strlen = len(my_string)
    new_string = []

    for i in range(strlen):
        if (('c' == my_string[i]) or ('C' == my_string[i])):
            continue
        else:
            new_string.append(my_string[i])

    return ("".join(new_string))

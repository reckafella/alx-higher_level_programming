#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    print x elements of a list
    """
    count = 0
    while (count < x):
        try:
            print("{}".format(my_list[count]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count

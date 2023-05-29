#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    print x elements of a list
    """
    count = 0
    for item in my_list:
        try:
            print("{:d}".format(item), end="")
            count += 1
        except (TypeError,):
            pass
    print()
    return count
#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count, index = 0, 0
    while index < x:
        try:
            print("{:d}".format(my_list[index]), end="")
            count += 1
            index += 1
        except (ValueError, TypeError):
            index += 1
    print()
    return count

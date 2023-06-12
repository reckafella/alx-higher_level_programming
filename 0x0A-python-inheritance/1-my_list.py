#!/usr/bin/python3

""" Class that inherits from "list" """


class MyList(list):
    """
    Class that inherits from list\
    and prints the list appended in ascending order
    
    Args:
        list (list): BaseClassName
    """
    my_list = []
    def __init__(self):
        self.my_list = []
        super().__init__()
    
    def print_sorted(self):
        print(sorted(self))

my_list = MyList
my_list.append(1)
my_list.append(2)

print(my_list)
my_list.print_sorted()
print(my_list)
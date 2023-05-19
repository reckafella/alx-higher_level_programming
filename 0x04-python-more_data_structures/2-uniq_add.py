#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    sum = 0

    for i in range(len(my_set)):
        sum += my_set[i]

    return sum

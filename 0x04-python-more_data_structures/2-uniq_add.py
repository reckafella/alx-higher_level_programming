#!/usr/bin/python3

def uniq_add(my_list=[]):
    no_dup = list(set(my_list))
    sum = 0

    for i in range(len(no_dup)):
        sum += no_dup[i]

    return sum

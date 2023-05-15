#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = []
    for i in range(len(tuple_a)):
        if ((len(tuple_a) < 2) or (len(tuple_b) < 2)):
                my_list.append(tuple_a[i] + tuple_b[i])
    return (tuple(my_list))

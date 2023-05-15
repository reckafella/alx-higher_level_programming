#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None

    a, b = 0, (len(my_list) - 1)

    while (b > 1):
        while (a < b):
            if (my_list[a] > my_list[a + 1]):
                temp = my_list[a]
                my_list[a] = my_list[a + 1]
                my_list[a + 1] = temp
            a += 1
        b -= 1

    return (my_list[-1])

#!/usr/bin/python3

import hidden_4

if __name__ == '__main__':
    names_list = dir(hidden_4)
    for i in range(len(names_list)):
        if (names_list[i].startswith("__")):
            continue
        else:
            print("{}".format(names_list[i]))

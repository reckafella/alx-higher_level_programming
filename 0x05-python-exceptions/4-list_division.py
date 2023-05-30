#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div_res = 0
    result = []

    while index < list_length:
        try:
            div_res = (my_list_1[index] / my_list_2[index])
            index += 1
        except ZeroDivisionError:
            print("division by 0")
            div_res = 0
            index += 1
        except TypeError:
            print("wrong type")
            div_res = 0
            index += 1
        except IndexError:
            print("out of range")
            div_res = 0
            index += 1
        finally:
            result.append(div_res)
    return result

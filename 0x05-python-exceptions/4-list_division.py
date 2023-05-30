#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    index = 0
    div_res = 0
    result = []

    while index < list_length:
        try:
            div_res = (my_list_1[index] / my_list_2[index])
            result.append(div_res)
            index += 1
        except ZeroDivisionError:
            print("division by 0")
            result.append(1)
            index += 1
        except TypeError:
            print("wrong type")
            result.append(2)
            index += 1
        except IndexError:
            print("out of range")
            result.append(0)
            index += 1
        finally:
            return result

#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in my_list:
        max = my_list[0]
        if i > max:
            max = i
    return max

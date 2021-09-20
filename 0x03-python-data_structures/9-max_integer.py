#!/usr/bin/python3
def max_integer(my_list=[]):
    total = 0
    for i in my_list:
        if i > total:
            total = i
    return total
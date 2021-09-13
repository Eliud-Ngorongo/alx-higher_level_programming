#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for numbers in reversed(my_list):
        print("{:d}".format(numbers))


list = [5, 4, 3, 2, 1]
print_reversed_list_integer(list)
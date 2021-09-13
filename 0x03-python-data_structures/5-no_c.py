#!/usr/bin/python3
def no_c(my_string):
    newstring = ''
    for c in my_string:
        if c != 'C' and c != 'c':
            newstring = newstring + c
    return newstring

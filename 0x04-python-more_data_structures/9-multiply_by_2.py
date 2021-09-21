#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for elm in a_dictionary:
       a_dictionary[elm]= a_dictionary[elm] * 2
    return a_dictionary

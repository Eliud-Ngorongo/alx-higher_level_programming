#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for elm in new:
       new[elm]= new[elm] * 2
    return  new

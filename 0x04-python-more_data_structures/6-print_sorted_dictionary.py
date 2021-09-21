#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new = dict(sorted(a_dictionary.items()))
    for elm in new:
        print(elm, ":", new[elm])

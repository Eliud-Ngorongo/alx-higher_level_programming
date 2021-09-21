#!/usr/bin/python3

# dicto = { 'language': "C", 'number': 89, 'track': "Low level" }

# dicto[key] = value

# print(dicto)

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary


dicto = { 'language': "C", 'number': 89, 'track': "Low level","class":2 }



def simple_delete(a_dictionary, key=""):
    if key not in a_dictionary:
        return a_dictionary 
    else:
        a_dictionary.pop(key)
        return a_dictionary

print(simple_delete(dicto, "same"))


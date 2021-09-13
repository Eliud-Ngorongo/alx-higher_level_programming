#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    else:
        return(my_list[idx])   

# This can also be written as:
#                        return(my_list[idx] if 0 <= idx < len(my_list)else None)    
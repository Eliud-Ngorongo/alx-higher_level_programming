#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        return(my_list[idx])


list = [1, 2, 6, 89]
idx = 5
print("Element at index {} is {}".format(idx, element_at(list, idx)))
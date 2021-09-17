#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1] + tuple_b[1]
        return (first, second)
    elif len(tuple_a) > 2 and len(tuple_b) > 2:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1] + tuple_b[1]
        return (first, second)
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_a) < 2 or len(tuple_b) < 2:
        first = tuple_a[0] + tuple_b[0]
        second = tuple_a[1]
        return (first, second)
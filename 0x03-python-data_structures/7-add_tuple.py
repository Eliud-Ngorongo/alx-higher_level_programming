#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple = ()
    z = (0, 0)
    tup1 = tuple_a + z
    tup2 = tuple_b + z
    first = tup1[0] + tup2[0]
    second = tup1[1] + tup2[1]
    return (first, second)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_length = max(len(tuple_a), len(tuple_b))
    new_tuple = []
    for i in range(max_length):
        element_a = tuple_a[i] if i < len(tuple_a) else 0
        element_b = tuple_b[i] if i < len(tuple_b) else 0
        sum_of_elements = element_a + element_b
        new_tuple.append(sum_of_elements)
    return tuple(new_tuple)

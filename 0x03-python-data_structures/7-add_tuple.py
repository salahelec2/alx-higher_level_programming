#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    max_length = max(len(tuple_a), len(tuple_b))
    new_tuple = tuple((tuple_a[i] if i < len(tuple_a) else 0) + (tuple_b[i] if i < len(tuple_b) else 0) for i in range(max_length))
    return new_tuple

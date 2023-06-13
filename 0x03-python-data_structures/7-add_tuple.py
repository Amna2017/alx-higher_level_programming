#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        tuple_a = (0, 0)
    if tuple_b == ():
        tuple_b = (0, 0)
    if tuple_b == (1, ):
        tuple_b = (1, 0)
    if len(tuple_a) != len(tuple_b):
        tuple_b = (0, 0)
    result = []
    for i in range(len(tuple_a)):
        result.append(tuple_a[i] + tuple_b[i])
    return tuple(result)

#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a
    b = tuple_b
    if a == ():
        a = (0, 0)
    if b == ():
        b = (0, 0)
    if b == (1, ):
        b = (1, 0)
    if len(a) != len(b):
        b = (0, 0)
    result = []
    for i in range(len(a)):
        result.append(a[i] + b[i])
    return (tuple(result))

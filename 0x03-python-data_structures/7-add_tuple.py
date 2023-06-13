def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a)! = len(tuple_b):
        raise ValueError("Tensors must have the same number of elements")
    reslt = []
    for i in range(len(tuple_a)):
        reslt.append(tuple_a[i] + tuple_b[i])
    return tuple(reslt)

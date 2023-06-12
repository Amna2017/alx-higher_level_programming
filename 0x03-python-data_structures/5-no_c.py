#!/usr/bin/python3
def no_c(my_string):
    list_ = []
    num = len(my_string)
    for ff in range(num):
        if ord(my_string[ff]) == 99 or ord(my_string[ff]) == 67:
            continue
        else:
            list_.append(my_string[ff])
    yy = ''.join(list_)
    return yy

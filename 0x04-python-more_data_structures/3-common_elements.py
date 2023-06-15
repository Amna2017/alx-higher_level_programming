#!/usr/bin/python3
def common_elements(set_1, set_2):
    st_1 = list(set_1)
    st_2 = list(set_2)
    uniq = []
    for x in st_1:
        if x in st_2:
            uniq.append(x)
    return uniq

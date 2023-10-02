#!/usr/bin/python3
'''Find peak in list of unsorted integers'''


def find_peak(list_of_integers):
    '''Find peak in list unsorted integer'''
    list_of_integers = sorted(list_of_integers)
    return list_of_integers[-1]

#!/usr/bin/python3
""" my files """


def read_file(filename=""):
    "my func """
    with open('UTF8', encoding="utf-8") as f:
        ii = f.read()
        print("{:s}".format(ii))

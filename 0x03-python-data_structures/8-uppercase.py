#!/usr/bin/python3
def uppercase(str):
    leng = len(str)
    for xx in range(leng):
        yy = str[xx]
        if ord(yy) >64 and ord(yy) < 90:
            print(yy, end="")
        else:
            print("{:s}".format(chr(ord(yy) - 32)), end="")

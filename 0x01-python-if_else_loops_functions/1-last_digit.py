#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = len(str(number))
y = str(number)
last_d = int(y[x-1])
if last_d > 5:
    print("last digit of {:s} is {:d} and is greater than 5".format(y, last_d))
elif last_d == 0:
    print("last digit of {:s} is {:d} and is 0".format(y, last_d))
elif last_d < 6 and last_d != 0:
    print("last digit of {:s} is {:d} and is less than 6 and not 0\
            ".format(y, last_d))

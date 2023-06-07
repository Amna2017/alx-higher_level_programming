#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = len(str(number))
y = str(number)
last_d = int(y[x-1])
if last_d > 5:
    print("last digit of {:s} is {:d} and is grea\
ter than {:d}".format(y, last_d, 5))
elif last_d == 0:
    print("last digit of {:s} is {:d} and is {:d}".format(y, last_d, 0))
elif last_d < 6 and last_d != 0:
    print("last digit of {:s} is {:d} and is less\
 than {:d} and not {:d}".format(y, last_d, 6, 0))

#!/usr/bin/python3
for i in range(122, 96, -1):
    # If the ASCII code is odd, print the lowercase letter
    if i % 2 != 0:
        print("{:c}".format(i), end='')
    # If the ASCII code is even, print the uppercase letter
    else:
        print("{:c}".format(i - 32), end='')

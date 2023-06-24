#!/usr/bin/python3
def uppercase(str):
    # Loop through each character in the string
    for c in str:
        # If the character is a lowercase letter, convert it to uppercase
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        # Print the character without a new line
        print("{}".format(c), end='')
    # Print a new line at the end
    print()

#!/usr/bin/python3
def print_last_digit(number):
    # Get the absolute value of the number to handle negative inputs
    number = abs(number)
    # Get the last digit of the number using the modulo operator
    last_digit = number % 10
    # Print the last digit without a new line
    print("{}".format(last_digit), end='')
    # Return the value of the last digit
    return last_digit

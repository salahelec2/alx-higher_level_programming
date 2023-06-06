#!/usr/bin/python3
def print_last_digit(number):
    last_digit = int(str(number)[-1])
    return last_digit if number >= 0 else last_digit * -1

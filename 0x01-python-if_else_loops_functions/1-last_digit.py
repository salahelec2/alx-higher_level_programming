#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
print(
    "Last digit of %s is %s " % (number, last_digit)
    + (
        "and is greater than 5"
        if last_digit > 5
        else "and is 0"
        if last_digit == 0
        else "and is less than 6 and not 0"
        if last_digit < 6
        else " "
    )
)

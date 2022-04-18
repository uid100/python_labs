#!/usr/bin/env python3

# lab04 ex1b
# Factorial.py

# variables
factorial = 0
i = 1
result = 1

# input - get user number and exponent from user
factorial = int(input ("Enter a number: "))


# just for fun, we'll do this with a for loop
for i in range(1, factorial + 1, 1):
    result = result * i;

print("The result is " + str(result))
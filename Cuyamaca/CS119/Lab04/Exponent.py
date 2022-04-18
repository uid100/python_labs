#!/usr/bin/env python3

# lab04 ex1a
# Exponent.py

# variables and constants
number = 0
exponent = 0

# input - get user number and exponent from user
number = int(input("Enter a number: "))
exponent = int(input ("Enter the exponent: "))
i = 0
result = 1

# Make sure the loop body code is indented 4 spaces!
# Also, note the colon (:)
# The Ctrl-c key combination will break you out of an endless loop
# Print to the console
while i < exponent:
    result = result * number
    i += 1 # Be sure to change the loop control variable!

# <-- unindent after while loop code block is complete
print("The result is " + str(result))
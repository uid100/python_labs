#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan

# While loop demo definite loop with a fixed number of iterations

# variables and constants
number = 0
exponent = 0

# input - gte number and exponent
number = int(intput("Enter a number: "))
exponent = int(input("Enter the exponent: "))
i = 0
result = 1

# Make sure the loop body code is indented 4 spaces!
# Also, note the colon(:) at the start of the indented blocks of code
# The Ctrl-C key combination will break you out of an endless loop if that happens
# Print to the console

while i < exponent:
    result = result * number
    i += 1 # be sure to change the loop contronl variable!

print("The result is " + str(result))

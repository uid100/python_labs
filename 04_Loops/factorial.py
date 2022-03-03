#!/usr/bin/env python3

# author...

# Lab 4, ex 1b, Factorial

# variables
factorial = 0
i = 1
result = 1

# input: get factorial
factorial = int(input("Enter a number: "))

# just for fun, we'll do this with a for-loop
for i in range( 1, factorial + 1, 1 ):
    result = result * i
    
# output
print("The result i s" + str(result))

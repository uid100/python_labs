#!/usr/bin/env python3

# investment.py 

amount = float(input("how much each month: "))
years = int(input("enter number of years: "))
APR = float(input("interest rate: "))

period = 0
balance = 0.0

term = years * 12
interest_rate = APR / 100 / 12

while period < term:
    balance += amount 
    interest = balance * interest_rate
    balance += interest
    period = period + 1
    print( f"month: {period:2d} balance: ${balance:7.2f}" )

balance = 0
for period in range(0,years*12,1):
    balance += amount 
    interest = balance * interest_rate
    balance += interest
    period = period + 1
    print( f"month: {period:2d} balance: ${balance:7.2f}" )
    

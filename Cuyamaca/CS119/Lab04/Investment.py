#!/usr/bin/env python3

# Invest.py
# Lab04 ex2

#inputs
balance = 0.0
total_interest = 0.0
monthly_deposit = float(input("monthly deposit: "))
annual_percentage_rate = float(input("APR: "))
rate = annual_percentage_rate / 12 / 100
term_in_years = int(input("how many years: "))
term = term_in_years * 12

#process
print("mo\tinterest\tbalance")
for month in range(1,term+1,1):
    balance += monthly_deposit
    interest = balance * rate
    balance += interest
    print(f'{month:2d}\t${interest:5.2f}\t${balance:5.2f}')
    total_interest += interest

#output
print(f'total invested: {term * monthly_deposit:8.2f}')
print(f'interest earned: {total_interest:8.2f}')
print(f'final balance: {balance:8.2f}')
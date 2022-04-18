#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 03, Ex 1

# Portrait Studio Service Calculator

import locale
locale.setlocale(locale.LC_ALL, "en_us") 

# constants
SURCHARGE_PCT = 1.2
SUNDAY = 1
SATURDAY = 7

# variables
base_price = 0.0
day_of_week = 0
last_name = ""
num_subjects = 0

# input
last_name = input("Enter Last Name: ")
num_subjects = int(input("How many people? "))
day_of_week = int(input("day of week (enter 1 for Sunday, 2 for Monday..., 7 for Saturday "))



# processing

# output
print("Last name: " + last_name )
print("Total price: " + locale.currency(base_price, grouping=True))

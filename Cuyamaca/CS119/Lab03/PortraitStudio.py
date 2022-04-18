#!/usr/bin/env python3

# Lab3ex1

import platform
import locale

if platform.system().startswith('Windows'):
    locale.setlocale(locale.LC_ALL, 'en-US') # PC
else:
    locale.setlocale(locale.LC_ALL, 'en_US') # Mac/Linux/...and

#declare variables and constants
SURCHARGE_PCT = 1.2
SUNDAY = 1
SATURDAY = 7
base_price = 0.0
day_of_week = 0
last_name = ""
num_subjects = 0

#input
last_name = input("Enter last name: ")
num_subjects = int(input("Enter number of subjects: "))
day_of_week = int(input("Day of week (1=Sun, 2=Mon ... 7=Sat): "))

#process
if num_subjects == 1:
    base_price = 100.0
elif num_subjects == 2:
    base_price = 130.0
elif num_subjects == 3:
    base_price = 150.0
elif num_subjects == 4:
    base_price = 165.0
elif num_subjects == 5:
    base_price = 175.0
elif num_subjects == 6:
    base_price = 180.0
else:
    base_price = 185.0

#add surcharge for weekends
if day_of_week == 1 or day_of_week == 7:
    base_price = base_price * SURCHARGE_PCT

#output
print("Last name: " + last_name)
print("Total price: " + locale.currency(base_price, grouping=True))


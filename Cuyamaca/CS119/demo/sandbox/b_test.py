#!user/bin/env python3

# Cuyamaca College CS 119
# Kimberly Cook
# Lab 7 Exercise 4 test

from burger import Burger

# input is fine if you want the user's opinion... but we're testing, so let's set these.

name = "Bob"  # input("Enter your name: ")
# let the object set the order #
# order_num = input("Enter order number: ")
b_type = "small_monster"  # input("Enter type of burger: ")
qty = 3  # int(input("Enter quantity: "))
# my_order = Burger(name, order_num, b_type, qty)
Bobs_order = Burger(name, b_type, qty)

# and since we're testing... let's add a few more.
# in fact, I don't even need to use variables... just set the arguments here.
Kimberlys_order = Burger("Kimberly", "plain", 2)
Dans_order = Burger("Dan", "Monster", 5)
Jims_order = Burger("Jim", "nutin_special", 1)

print()
print(Bobs_order.to_string() + '\n\n\t-------\n')
print(Kimberlys_order.to_string() + '\n\n\t-------\n')
print(Dans_order.to_string() + '\n\n\t-------\n')
print(Jims_order.to_string() + '\n\n\t-------\n')

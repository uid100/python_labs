#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 7, Ex 1

# Magazine Test Fixture
from Magazine import Magazine

name = "Smith"  # input("Enter name of subscriber: ")
title = "Wired"  # input("Name of the magazine: ")
num_months = 8  # int(input("how many months left: "))

my_magazine = Magazine(name, title, num_months)

print(my_magazine.to_string())
# print(Magazine.to_string(my_magazine))

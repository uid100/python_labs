#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 06 Ex 1

# Methods.py contains library of reusable methods:
#   get_float_val(prompt)
#   get_int_val(prompt)
#   is_float(x)
#   is_integer(x)
#   find_string(list,search)
#   find_int(list,x)


def get_float_val(prompt):
    is_num = False
    str_val = input(prompt)

    while is_num == False:
        try:
            value = float(str_val)
            is_num = True
        except:
            print(str_val + " is not a float!")
            str_val = input(prompt)
    return value


def get_int_val(prompt):
    is_num = False
    str_val = input(prompt)

    while is_num == False:
        try:
            value = int(str_val)
            is_num = True
        except:
            print(str_val + " is not a int!")
            str_val = input(prompt)
    return value


def is_float(value):
    try:
        num = float(value)
        return True
    except:
        return False


def is_integer(value):
    try:
        num = int(value)
        return True
    except:
        return False


def find_string(the_list, find_val):
    list_len = len(the_list)
    found = False
    i = 0
    idx = -1
    find_val = str(find_val)

    while i < list_len and found == False:
        if find_val.upper() == the_list[i].upper():
            idx = i
            found = True
        i += 1
    return idx


def find_int(the_list, find_val):
    list_len = len(the_list)
    found = False
    i = 0
    idx = -1

    while i < list_len and found == False:
        if find_val == the_list[i]:
            idx = i
            found = True
        i += 1
    return idx


if __name__ == "__main__":
    test_values = [42, 3.14, "3.9.0", "TurTle", "SNAKE", "dog", "GOAT"]
    animals = ["goat", "ZEBRA", "HorsE", "foX", "dog", "Cat"]
    results = [5, 7, 14, 75, 42, 1024, 512, 3]

    #get_float_val("Enter a floating point number: ")
    #get_int_val("Enter a valid integer: ")

    for x in test_values:
        print(f"{x} is a valid float? ", is_float(x))
        print(f"{x} is an integer?", is_integer(x))
        print(f"{x} is in string list at: # ", find_string(animals, x))
        print(f"{x} is in integer list at: # ", find_int(results, x))

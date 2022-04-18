#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 06, Ex 1

import Methods as m

def main():
    # test our library of methods
    float_val = m.get_float_val("Enter a floating point number: ")
    print("Float value (from our method) " + str(float_val) + " was entered")

    int_val = m.get_int_val("Enter a valid integer: ")
    print("Integer (returned from method) " + str(int_val) + " was entered")

    str_val = input("Enter another float: ")
    result = m.is_float(str_val)
    if result == True:
        print( str_val + " is a float!")
    else:
        print( str_val + " is NOT a float.")

    # also add test for "is_integer()" !!!
    
    my_list = ["goat", "ZEBRA", "HorsE", "foX", "dog", "Cat"]
    value = input("Enter a value to find: ")

    index = m.find_string(my_list, value)
    if index >=0:
        print("Yes it's there! at index: ", str(index))
    else:
        print( value + " NOT FOUND!")

    # Add test for find_int()!!!
        
if __name__ == "__main__":
    main()

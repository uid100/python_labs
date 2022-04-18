#!/usr/bin/env python3

# lab 8 ex 1 Automobile test fixture

from Convertible import Convertible

def main():
    vin = "ABAB1958"
    make = "Chevrolet"
    model = "Corvette"
    color = "Red"
    yn = "yes"

    if yn.upper() == "YES":
        top_up = True
    else:
        top_up = False

    my_car = Convertible(vin, make, model, color, top_up)
    print(my_car.to_string())

if __name__=="__main__":
    main()
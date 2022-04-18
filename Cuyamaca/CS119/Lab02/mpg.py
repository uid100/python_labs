#!/usr/bin/env python3

# Lab 02; Ex 2
# Gas Mileage Calculator

gallons_purchased = float(input("\n\tTotal gallons purchased: "))
cost_per_gallon = float(input("\tCost Per Gallon: $"))
distance_driven = float(input("\tTotal miles driven? "))

total_fuel_cost = gallons_purchased * cost_per_gallon
miles_per_gallon = distance_driven / gallons_purchased
cost_per_mile = total_fuel_cost / distance_driven

print( f"\n\t{miles_per_gallon:.1f} mpg" + \
       f"\n\t${total_fuel_cost:.2f} total fuel cost" + \
       F"\n\tcost: {cost_per_mile:.3f} per mile" )
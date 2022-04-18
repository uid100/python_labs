#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 7, Ex 2

# Pizza class test fixture
from Pizza import Pizza

# create pizza orders with test data
lunch_pizza_order = Pizza("sausage & mushroom", "small", 1)
office_pizza_order = Pizza("pepperoni", "large", 6)
dinner_for_two = Pizza("works", "medium", 1)
late_night_pizza = Pizza("chef special", "small", 1)

# display results
print()
print("lunch:\n\t" + lunch_pizza_order.to_string() + "\n")
print(f"check the price:  ${lunch_pizza_order.calculate_price():.2f}")
print(f"this pizza is:  {lunch_pizza_order.get_toppings()}")


print("working lunch:\n\t" + office_pizza_order.to_string() + "\n")
print(f"check the price:  ${office_pizza_order.calculate_price():.2f}")

print("date night:\n\t" + Pizza.to_string(dinner_for_two) + "\n")
print(f"check the price:  ${dinner_for_two.calculate_price():.2f}")

print("kids are asleep:\n\t" + Pizza.to_string(late_night_pizza) + "\n")
print(f"\tcheck the price:  ${late_night_pizza.calculate_price():.2f}\n\n")

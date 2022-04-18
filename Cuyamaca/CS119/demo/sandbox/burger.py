#! user/bin/env python3

# Cuyamaca College
# Kimberly Cook
# CSIS 119 Lab 7 Burger

import Methods as m


class Burger:
    # set order_num to a class variable and it will be usable inside the class
    # as long as the application is running!
    order_num = 100

    __burger_types = ["Monster", "small_monster", "nutin_special", "plain"]
    __prices = [6.00, 4.95, 2.35, 1.99]

    def __init__(self, name, b_type, qty):
        Burger.order_num += 1  # new order, increment the order number.
        self.__order_num = Burger.order_num

        self.__name = name

        # don't need this... the setter has logic we can use instead.
        # self.__qty = qty
        self.set_qty(qty)

        self.set_b_type(b_type)  # use the setter here.
        self.calculate_price()  # ... and here.... not:  self.__price = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_order_num(self):
        return self.__order_num

    def set_order_num(self, order_num):
        self.__order_num = order_num

    def get_b_type(self):
        return self.__b_type

    def set_b_type(self, b_type):
        idx = m.find_string(self.__burger_types, b_type)
        if idx >= 0:
            self.__price = Burger.__prices[idx]
            self.__b_type = Burger.__burger_types[idx]
        else:
            self.__price = Burger.__prices[0]
            self.__b_type = Burger.__burger_types[0]

    def get_qty(self):
        return self.__qty

    def set_qty(self, qty):
        if qty < 0:
            qty = 0
        self.__qty = qty

    def get_price(self):
        return self.__price

    def calculate_price(self):
        return self.__price * float(self.__qty)

    def to_string(self):
        ext_price = self.calculate_price()
        return "Hello " + self.__name \
            + "!  Order number: " + str(self.__order_num) + "\n" \
            + str(self.__qty) + " " \
            + self.__b_type.upper() + f" burger{'s' if int(self.__qty) > 1 else ''} " \
            + f"( @ ${self.__price:.2f} each )\n" \
            + f"\nYour total is: ${ext_price:.2f}"

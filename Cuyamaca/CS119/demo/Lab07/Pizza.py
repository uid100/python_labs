#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 7, Ex 2

# Pizza Class implementation

import Methods


class Pizza:
    __sizes = ["small", "medium", "large"]
    __prices = [8.00, 10.00, 12.00]
    order_number = 100

    def __init__(self, toppings, size, qty):
        Pizza.order_number += 1
        self.__toppings = toppings
        self.__qty = qty
        self.__price = 0
        self.__size = size
        self.set_size(size)
        self.__order_num = Pizza.order_number

    def get_toppings(self):
        return self.__toppings

    def set_toppings(self, toppings):
        self.__toppings = toppings

    def get_qty(self):
        return self.__qty

    def set_qty(self, qty):
        if qty < 0:
            qty = 0
        self.__qty = qty

    def get_size(self):
        return self.__size

    def set_size(self, size):
        idx = Methods.find_string(self.__sizes, size)
        if idx >= 0:
            self.__price = self.__prices[idx]
            self.__size = size
        else:
            self.__price = self.__prices[0]
            self.__size = self.__sizes[0]

    def calculate_price(self):
        return self.__price * float(self.__qty)

    def to_string(self):
        ext_price = self.calculate_price()
        return f"{self.__order_num} Toppings: " + self.__toppings \
            + " size: " + self.__size \
            + f" quantity: {self.__qty}" \
            + f" Total price: ${ext_price:.2f}"

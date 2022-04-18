#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab ##, Ex #

import Methods


class Pizza:
    __sizes = ["S", "M", "L"]
    __prices = [8.00, 10.00, 12.00]

    def __init__(self, pizza_toppings, size, quantity):
        self.__price = 0
        self.__toppings = pizza_toppings
        self.__qty = quantity
        self.set_size(size)

    def set_size(self, order_size):
        idx = Methods.find_string(Pizza.__sizes, order_size)
        self.__price = Pizza.__prices[0]
        self.__size = Pizza.__sizes[0]
        if idx >= 0:
            self.__price = Pizza.__prices[idx]
            self.__size = Pizza.__sizes[idx]

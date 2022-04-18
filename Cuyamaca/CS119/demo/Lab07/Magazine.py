#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 7, Ex 1

# Magazine class implementation

class Magazine:
    def __init__(self, subscr_name, mag_title, months_left):
        self.__subscriber_name = subscr_name
        self.__magazine_title = mag_title
        self.__months_remaining = months_left

    def get_subscriber_name(self):
        return self.__subscriber_name

    def set_subscriber_name(self, name):
        self.__subscriber_name = name

    def get_magazine_title(self):
        return self.__magazine_title

    def set_magazine_title(self, title):
        self.__magazine_title = title

    def get_months_remaining(self):
        return self.__months_remaining

    def set_months_remaining(self, title):
        self.__months_remaining = title

    def to_string(self):
        return "Subscriber name: " + self.__subscriber_name \
            + " Magazine title: " + self.__magazine_title \
            + " Months remaining: " + str(self.__months_remaining)

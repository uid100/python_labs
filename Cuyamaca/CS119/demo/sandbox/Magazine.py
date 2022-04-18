#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 07, Ex 1

# Magazine class

class Magazine:
    def __init__(self, subscriber_name, magazine_title, months_remaining):
        self.__subscriber_name = subscriber_name
        self.__magazine_title = magazine_title
        self.__months_remaining = months_remaining

    def get_subscriber_name(self):
        return self.__subscriber_name

    def set_subscriber_name(self, subscriber_name):
        self.__subscriber_name = subscriber_name

    def get_magazine_title(self):
        return self.__magazine_title

    def set_magazine_title(self, magazine_title):
        self.__magazine_title = magazine_title

    def get_months_remaining(self):
        return self.__months_remaining

    def set_months_remaining(self, months_remaining):
        self.__months_remaining = months_remaining

    def to_string(self):
        # return "Name: " + self.__subscriber_name \
        return "Name: " + self.__subscriber_name \
            + " Title:" + self.__magazine_title \
            + " " + str(self.__months_remaining) + " more months."


if __name__ == "__main__":
    # test_data
    name = ["Smith", "Johnson", "Williams", "Brown"]
    magazines = ["Better Homes & Gardens",
                 "Game Informer Magazine", "Wired", "Time"]
    how_long = [5, 6, 7, 8]

    i = 0
    while i < len(name):
        next_magazine = Magazine(name[i], magazines[i], how_long[i])
        if next_magazine.get_subscriber_name() == name[i] and \
                next_magazine.get_magazine_title() == magazines[i] and \
                next_magazine.get_months_remaining() == how_long[i]:
            print(f"{next_magazine.to_string()}", end=' ')
            next_magazine.set_subscriber_name("Dr. " + name[i])
            next_magazine.set_magazine_title(
                next_magazine.get_magazine_title().upper())
            next_magazine.set_months_remaining(99)
            if next_magazine.get_subscriber_name() == "Dr. " + name[i] and \
                    next_magazine.get_magazine_title() == magazines[i].upper() and \
                    next_magazine.get_months_remaining() == 99:
                print(" PASS")

        else:
            print(f"FAIL {i}")
        i += 1

#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 7, Ex 1

# Magazine class test fixture

from Magazine import Magazine


def get_user_inputs():
    name = "Smith"  # input("Enter subscriber name: ")
    title = "Newsweek"  # input("Enter magazine title: ")
    months_left = 24  # int(input("Enter months remaining: "))
    return name, title, months_left


def main():
    subscriber, publication, term = get_user_inputs()
    my_magazine = Magazine(subscriber, publication, term)
    print(Magazine.to_string(my_magazine))


if __name__ == "__main__":
    main()

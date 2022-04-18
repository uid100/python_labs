#!/usr/bin/env python3

# lab 8 ex 5 Student class implementation

from Person import Person

class Student(Person):
    def __init__(self, name, address, age):
        super().__init__(name, address, age)
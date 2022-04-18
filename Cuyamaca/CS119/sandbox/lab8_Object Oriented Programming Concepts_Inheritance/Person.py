#!/usr/bin/env python3

# lab 8 ex 5 Person class implementation

class Person:
    def __init__(self,name,address,age):
        self._name = name
        self._address = address
        self._age = age

    # accessors
    def get_name(self):
        return self._name
    def set_name(self,name):
        self._name = name
    
    def get_address(self):
        return self._address
    def set_address(self,address):
        self._address = address

    def get_age(self):
        return self._age
    def set_age(self,age):
        self._age = age

    # public instance methods
    def to_string(self):
        return f'{self._name} (age:{self._age})\n{self._address}'

    
##### Unit Test #####
if __name__=="__main__":
    TestData = ('''
        {
            "Guitar": [
                {
                    "name": "Steve Howe",
                    "age": 74,
                    "address": "10 Downing, London, United Kingdom"
                },
                {
                    "name": "Eddie Van Halen",
                    "address": "1600 Pennsylvania Avenue, Washington, D.C.",
                    "age": 65
                },
                {
                    "name": "Jimi Hendrix",
                    "age": 28,
                    "address": "Yasgur's Dairy Farm, Bethel, NY"
                },
                {
                    "name": "Eric Clapton",
                    "address": "3 Abbey Rd, London, United Kingdom",
                    "age": 76
                },
                {
                    "name": "Stevie Ray Vaughan",
                    "address": "1 AT&T Way, Arlington, TX",
                    "age": 46
                }
            ]
        }
    ''')

    import json
    band = json.loads(TestData)

    for x in band['Guitar']:
        musician = Person(x['name'],x['address'],x['age'])
        print( musician.to_string()+"\n" )

#!/usr/bin/env python3

# lab 8 ex 3 Player class implementation

class Player:
    def __init__(self, name, number):
        self._name = name
        self.set_number(number)

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_number(self):
        return self._number
    def set_number(self, number):
        MIN_PLAYER_NUMBER = 1
        MAX_PLAYER_NUMBER = 9999

        # validate player number
        if number >= MIN_PLAYER_NUMBER and number <= MAX_PLAYER_NUMBER:
            self._number = number
        else:
            self._number = 0

    # public instance method(s)
    def to_string(self):
        return f"\t{self._number:4d}. {self._name}"


##### Unit Test #####
if __name__=="__main__":
    TestData = ('''
        {
            "Players": [
                {
                    "name": "John",
                    "number": 1
                },
                {
                    "name": "Paul",
                    "number": 2
                },
                {
                    "name": "George",
                    "number": 3
                },
                {
                    "name": "Ringo",
                    "number": 4
                },
                {
                    "name": "Really Big Number Test",
                    "number": 12345
                }
            ]
        }
    ''')

    import json
    band = json.loads(TestData)

    for x in band['Players']:
        musician = Player(x['name'],x['number'])
        print( musician.to_string() )


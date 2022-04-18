#!/usr/bin/env python3

# lab 8 ex 1 Automobile class implementation

# properties are public by default
# use _ single underscore for protected
# use __ double underscore for private
class Automobile:
    def __init__(self, vin, make, model, color):
        self._vin = vin
        self._make = make
        self._model = model
        self._color = color
    
    # define accessors (getters & setters) for properties
    def get_vin(self):
        return self._vin
    def set_vin(self, vin):
        self._vin = vin

    def get_make(self):
        return self._make
    def set_make(self, make):
        self._make = make

    def get_model(self):
        return self._model
    def set_model(self, model):
        self._model = model

    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color

    # instance method(s)
    def to_string(self):
        return f"Color: {self._color:8}" \
            + f" Make: {self._make:10}" \
            + f" Model: {self._model:8}" \
            + f" VIN: {self._vin:10}"

if __name__=="__main__":
    # test_car = Automobile("abcd1234", "Morris", "Minor", "Red")
    # print(test_car.to_string())
    # test_car = Automobile("wxyz9876", "MG", "A", "White")
    # print(test_car.to_string())

    TestData = (
    '{"Automobiles": ['
    '   {'
    '       "vin": "lmnop555",'
    '       "make": "Volkswagen",'
    '       "model": "Type II",'
    '       "color": "Blue"'
    '   },'
    '   {'
    '       "vin": "abcd1234",'
    '       "make": "Morris",'
    '       "model": "Minor",'
    '       "color": "Red"'
    '   },'
    '   {'
    '       "vin": "2fast04u",'
    '       "make": "Alpine",'
    '       "model": "Sunbeam",'
    '       "color": "Yellow"'
    '   },'
    '   {'
    '       "vin": "wxyz9876",'
    '       "make": "MG",'
    '       "model": "A",'
    '       "color": "White"'
    '   },'
    '   {'
    '       "vin": "J8675309",'
    '       "make": "Shelby",'
    '       "model": "Cobra",'
    '       "color": "Blue"'
    '   }'
    ']}'
    )

    import json
    data = json.loads(TestData)
    for car in data['Automobiles']:
        # print( car )
        test_car = Automobile(car['vin'], car['make'], car['model'], car['color'])
        print( test_car.to_string() )

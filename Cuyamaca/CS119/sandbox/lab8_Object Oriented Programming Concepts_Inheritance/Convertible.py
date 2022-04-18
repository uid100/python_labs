#!/usr/bin/env python3

# lab 8 ex 1 Convertible class implementation

# Import the parent class
from Automobile import Automobile

class Convertible(Automobile):
    def __init__(self, vin, make, model, color, is_top_up):
        super().__init__(vin, make, model, color)
        self._is_top_up = is_top_up
    
    # define accessors (getters & setters) for properties
    def get_is_top_up(self):
        return self._is_top_up
    def set_is_top_up(self, is_top_up):
        self._is_top_up = is_top_up

    # public instance method(s)
    def fmt_top_status(self):
        status = "No" # default
        if self._is_top_up == True:
            status = "Yes"
        return status

    def to_string(self):
        return super().to_string() \
            + f" Is top up? {self.fmt_top_status()}"

if __name__=="__main__":
    # test_car = Convertible("ABAB1958", "Chevrolet", "Corvette", "Red", False)
    # print(test_car.to_string())

    TestData = ('''
{
    "Convertibles": [
        {
            "vin": "AAA12345",
            "make": "Ford",
            "model": "Mustang",
            "color": "Red",
            "top_closed": true
        },
        {
            "vin": "A1960356",
            "make": "Porsche",
            "model": "356",
            "color": "Green",
            "top_closed": false
        }
    ]
}
    ''')

    import json
    data = json.loads(TestData)
    for car in data['Convertibles']:
        # print( car )
        test_car = Convertible(car['vin'], car['make'], car['model'], car['color'], car['top_closed'])
        print( test_car.to_string() )

#!/usr/bin/env python3

# lab 8 ex 2 Race Car class implementation

# Import the parent class
from Automobile import Automobile

class RaceCar(Automobile):
    def __init__(self, vin, make, model, color, hp):
        super().__init__(vin, make, model, color)
        self._horse_power = hp
    
    # define accessors (getters & setters) for properties
    def get_horse_power(self):
        return self._horse_power
    def set_is_top_up(self, horse_power):
        self._horse_power = horse_power

    # public instance method(s)
    def fmt_horsepower(self):
        return f" {self._horse_power} hp!"

    def to_string(self):
        return super().to_string() \
            + self.fmt_horsepower()

if __name__=="__main__":
    test_car = RaceCar("G0G01980", "Acura", "NSX", "Red", 573)
    print(test_car.to_string())

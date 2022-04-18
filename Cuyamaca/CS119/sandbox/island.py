#!/usr/bin/env Python3

import random

weather = ["rainy", "cloudy", "windy", "sunny", "clear"]
deg_sym = '\xb0'

class Island:
    __names = ["Hawai'i", "Maui", "Moloka'i", "Lana'i", "Kaho'olawe", "O'ahu", "Kaua'i", "Ni'ihau" ]

    def __init__(self):
        self.__name = random.choice(Island.__names)
        idx = Island.__names.index(self.__name)
        self.__temperature = random.randint(70,80)
        n = len(weather)
        self.__sky = weather[self.__temperature%n]


    def to_string(self):
        return(f"{self.__name:10} : " \
            + f"{self.__temperature}{deg_sym}F" \
            + f"({ToCelsius(self.__temperature)}{deg_sym}C) " \
            + f"and {self.__sky}")

def ToCelsius(f):
    return int((f - 32) * 5/9)
def ToFahrenheit(c):
    return int((c * 9/5) + 32)

if __name__ == "__main__":
    i = 0
    count = 15

    print('\nvacation forecast')
    while i < count:
        destination = Island()
        print(f'\tday {i:2} {destination.to_string()}')
        i+=1
    print()
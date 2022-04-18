#!/usr/bin/env python3

# lab 08 ex.3 player class test fixture

from BaseballPlayer import BaseballPlayer
from BasketballPlayer import BasketballPlayer

name = "Tony Gwinn"
number = 19
batting_average = .338
position = "right fielder"

test_player = BaseballPlayer(name, number, position, batting_average)
print(test_player.to_string())

name = "Michael Jordan"
number = 12   # Bulls
position = "shooting guard"
free_throw_perc = 83.5

test_player = BasketballPlayer(name, number, position, free_throw_perc)
print(test_player.to_string())

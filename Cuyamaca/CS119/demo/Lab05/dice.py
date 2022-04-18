#!/usr/bin/env python3

# Cuyamaca College CS-119
# Dan Sullivan
# Lab 05, Ex 2

# Dice Game
# Roll 5 dice each for 2 players (computer and player) and count results and
# display winner.



import random

# constants
MAX_ROLLS = 5       # how many dice does each player roll?
MAX_DICE_VAL = 6    # 6 sides on the dice

roll_types = ["junk", "pair", "3 of a kind", "4 of a kind", "5 of a kind"]


# variables
pdice = [0,0,0,0,0]
cdice = [0,0,0,0,0]

ptally = [0,0,0,0,0,0]
ctally = [0,0,0,0,0,0]


#input  (get numbers from random generator)
i = 0
while i < MAX_ROLLS:
    roll_val = random.randint(1,MAX_DICE_VAL)
    pdice[i] = roll_val
    roll_val = random.randint(1,MAX_DICE_VAL)
    cdice[i] = roll_val
    i += 1    #  i = i + 1

# display the values (read the dice)
print("Player: ", end = " ")

i = 0
while i < len(pdice):
    print(pdice[i], end = " " )
    i += 1


print("Computer: ", end = " ")
i = 0
while i < len(cdice):
    print(cdice[i], end = " ")
    i += 1


#processing
# count the result of the dice rolls
i = 0
while i < MAX_ROLLS:
    ptally[ pdice[i] - 1] += 1
    ctally[ cdice[i] - 1] += 1
    i += 1


pmax = ptally[0]
cmax = ctally[0]

i = 1
while i < MAX_DICE_VAL:
    if pmax < ptally[i]:
        pmax = ptally[i]
    if cmax < ctally[i]:
        cmax = ctally[i]
    i += 1


#output
print("\nPlayer rolled: " + roll_types[pmax - 1])
print("Computer rolled: " + roll_types[cmax - 1])

#determine winner
if pmax > cmax:
    print("Player Wins!")
elif cmax > pmax:
    print("Computer Wins!")
else:
    print("Tie!")
    

    
    

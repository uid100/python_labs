#input
get how many rounds user wants to play
           
#input
roll_types = ( Junk, Fair, 3 of a kind, 4 of a kind, 5 of a kind )

# less detailed approach
get 5 dice rolls for the computer
get 5 dice rolls for the player

# OR more detailed pseudocode
for i = 0 to 4
    roll pDice [i] for player
    roll cDice [i] for computer
    display pDice [i] and cDice [i]
end for

# which of the above would be easier to code from?

# process - figure out what got rolled and who won
add a loop

display what player and computer rolled

# tally up the dice rolls so we can figure out pair, 3 of a king, etc
while i < MAX_ROLLS
    pTally[ pDice[i] - 1 ]++
    cTally[ cDice[i] - 1 ]++
end while

# now find the highest roll comdination (pair, 3 of a kind, etc.)
pMax = pTally[0]
cMax = cTally[0]

i = 1
while i < MAX_DICE_VAL
    if pMax < pTally[i] then
        pMax = cTally[i]
    end if

    if cMax < cTally [i] then
        cMax = cTally[i]
    end if
    i = i + 1
end while

# output display the type of roll, who won the round
display rollTypes[ pMax - 1 ] for the player
display rollTypes[ cMax - 1 ] for the computer

if pMax > cMax then
    display player wins
else if cMax > pMax then
    display computer wins
else
    display tie
end

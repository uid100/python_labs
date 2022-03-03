#!/usr/bin/env python3

# author...
# Lab 05, ex 1, parallel array search

# Create parallel lists of ZIP codes and the corresponding cities & states
zips = [53115,53125,53147,53184]
cities = ["Delevan","Fontana","Lake Geneva","Walworth"]
states = ["WI","WI","IL","IL"]

# other variables we need
zip_code = 0
city = "NOT FOUND"
state = ""
found = False
i = 0
list_len = len(zips) # get the array size for the upper bound of the loop

# input - get ZIP code
zip_code = int(input("Enter zip code: "))

# search the array
while i < list_len and not found:  # don't forget the colon (:) on a loop condition
    # test for a ZIP code match and indent the if(True) block
    if zip_code == zips[i]: don't forget the colon (:) on the if block
        # found a match!
        city = cities[i]
        state = states[i]
        found = True
    i = i + 1  # be sure to increment the loop counter
# end while


# output
print("ZIP: " + str(zip_code) + " City: " + city + " State: " + state )

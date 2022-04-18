#!/usr/bin/env python3

# CoinToss.py
# Lab04 ex.3

import random

MAX_FLIPS = 20
MAX_VAL = 2
count = 0

for i in range(1,MAX_FLIPS + 1, 1):
    flip = random.randint(0,1)
    if flip > 0:
        count += 1
    
print(f"Heads: {count:d} ({count/MAX_FLIPS*100:.1f}%)")
count = MAX_FLIPS - count
print(f"Tails: {count:d} ({count/MAX_FLIPS*100:.1f}%)")

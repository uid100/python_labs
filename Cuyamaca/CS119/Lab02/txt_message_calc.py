#!/usr/bin/env python3

# Lab 02; Ex 1
# Text Message Cost Calculator

cost_per_txt = 0.25 # per text message
taxrate = .09
num_txts = int(input("\n\tenter number of texts in billing period: "))

cost = num_txts * cost_per_txt
total_due = cost * (1 + taxrate)

print(f"\n\tBilling for month" + \
      f"\n\tTotal text messages: {num_txts:d}" + \
      f"   @ {cost_per_txt:.2f} ea" + \
      f"\n\tTotal cost: ${cost:,.2f}" + \
      f"\n\t{taxrate * 100:.2f}% tax = ${cost * taxrate:.2f}" + \
      f"\n\tTotal due:  ${total_due:,.2f}\n")
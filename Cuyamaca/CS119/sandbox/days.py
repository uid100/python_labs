#!/usr/bin/env python3

# days.py

from datetime import date
import calendar

def today():
    d = date.today()
    return calender.day_name[d.weekday()]


if __name__ == "__main__":
    print()
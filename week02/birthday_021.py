#!/usr/bin/env python3

import sys
import calendar

poems = [
    "Monday's child is fair of face.",
    "Tuesday's child is full of grace.",
    "Wednesday's child is full of woe.",
    "Thursday's child has far to go.",
    "Friday's child is loving and giving.",
    "Saturday's child works hard for a living.",
    "Sunday's child is fair and wise and good in every way."
]

days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

def get_bday(s):
    s = s.split()
    date = int(s[0])
    month = int(s[1])
    year = int(s[2])
    day = calendar.weekday(year, month, date)
    dayAndPoem = f'You were born on a {days[day]} and {poems[day]}'
    return dayAndPoem

for line in sys.stdin:
    print(get_bday(line))

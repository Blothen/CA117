#!/usr/bin/env python3

import sys

data = []
club_width = 0


for line in sys.stdin:
    data.append(line.split())

for item in data:
    club_data = item
    if len(club_data) == 11:
        club_name = club_data[1] + " " + club_data[2]
        if len(club_name) > club_width:
            club_width = len(club_name)
    elif len(club_data) == 12:
        club_name = club_data[1] + " " + club_data[2] + " " + club_data[3]
        if len(club_name) > len(club_width):
            club_width = len(club_name)
    print(club_width)

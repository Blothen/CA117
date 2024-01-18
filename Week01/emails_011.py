#!/usr/bin/env python3

import sys

for line in sys.stdin:
    left_side = line.split("@")
    email_name = left_side[0].split(".")
    right_side_email = email_name[1]
    for char in right_side_email:
        if char.isdigit():
            right_side_email = right_side_email.replace(char, "")
    print(email_name[0].capitalize() + " " + right_side_email.capitalize())

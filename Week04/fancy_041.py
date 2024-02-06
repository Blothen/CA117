#!/usr/bin/env python3

import sys

file = sys.argv[1].strip()
contacts = {}

with open(file, "r") as f:
    for line in f.readlines():
        tokens = line.strip().split()
        contacts[tokens[0]] = [tokens[1], tokens[2]]


for line in sys.stdin:
    line = line.strip()
    if line in contacts:
        print(f"Name: {line}")
        print(f"Phone: {contacts[line][0]}")
        print(f"Email: {contacts[line][1]}")
    else:
        print(f"Name: {line}")
        print("No such contact")

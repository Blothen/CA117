#!/usr/bin/env python3

import sys

file = sys.argv[1].strip()
best = -1
person = ""

try:
    with open(file, "r") as f:
        try:
            for line in f.readlines():
                tokens = line.split()
                if int(tokens[0]) > best:
                    best = int(tokens[0])
                    person = line.strip()
        except ValueError:
            print(f"Invalid mark {tokens[0]} encountered. Skipping.")
    tokens = person.split()
    name = ""
    for item in tokens[1:]:
        name = name + " " + item
    print(f"Best student: {name.lstrip()}")
    print(f"Best mark: {best}")
except FileNotFoundError:
    print(f"The {file:s} could not be opened.")
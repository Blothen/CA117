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
                    person = ' '.join([str(elem) for elem in tokens[1:]])
                elif int(tokens[0]) == best:
                    person = person +  ", " + ' '.join([str(elem) for elem in tokens[1:]])
        except ValueError:
            print(f"Invalid mark {tokens[0]} encountered. Skipping.")
    print(f"Best student(s): {person}")
    print(f"Best mark: {best}")
except FileNotFoundError:
    print(f"The {file:s} could not be opened.")

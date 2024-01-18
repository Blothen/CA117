#!/usr/bin/env python3

import sys

def check_suffix(string):
    es_tuple = ("ch", "sh", "x", "s", "z")
    y_nonsonants = ("ay", "ey", "iy", "oy", "uy")
    if string.endswith(es_tuple):
        string = string + "es"
        return string
    elif string.endswith("y") and string[len(string) -2:] not in y_nonsonants:
        string = string.replace("y", "ies")
        return string
    elif string.endswith("f"):
        string = string.replace("f", "ves")
        return string
    elif string.endswith("fe"):
        string = string.replace("fe", "ves")
        return string
    elif string.endswith("o"):
        string = string + "es"
        return string
    else:
        string = string + "s"
        return string

for line in sys.stdin:
    print(check_suffix(line.strip()))


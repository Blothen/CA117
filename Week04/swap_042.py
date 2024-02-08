#!/usr/bin/env python3

def swap_keys_values(dictionary):
    return dict((v, k) for k,v in dictionary.items())

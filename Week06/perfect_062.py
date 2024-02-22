#!/usr/bin/env python3

def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def get_proper_divisors(n):
    return [i for i in range(1, n - 1) if n % i == 0]


def is_perfect(n):
    values = get_proper_divisors(n)
    return sum(values) == n


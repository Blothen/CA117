#!/usr/bin/env python3

class CashRegister:
    def __init__(self, total=0, count=0):
        self.total = total
        self.count = count

    def __str__(self):
        return f'Items: {self.count}\nTotal: {self.total:.02f}'

    def add_item(self, item):
        self.total = self.total + item
        self.count += 1
        
    def clear(self):
        self.total = 0
        self.count = 0

#!/usr/bin/env python3

class BankAccount:
    def __init__(self, balance=0.00):
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount

    def __str__(self):
        if self.balance == 0.0:
            self.balance == 0.00
        output_balance = f'{self.balance:.02f}'
        return 'Your current balance is ' + output_balance + ' euro'

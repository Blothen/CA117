#!/usr/bin/env python3

class Lamp:
    def __init__(self, active=False):
        self.on = active
        
    def turn_on(self):
        if not self.on:
            self.on = True
            
    def turn_off(self):
        if self.on:
            self.on = False
            
    def toggle(self):
        if self.on:
            self.on = False
        else:
            self.on = True

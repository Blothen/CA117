#!/usr/bin/env python3

class Point:
    def set_attributes(self, x, y):
        self.x = float(x)
        self.y = float(y)
        
    def print_attributes(self):
        print(f'x: {self.x:.2f}')
        print(f'y: {self.y:.2f}')
        
    def reflect(self):
        self.x = -self.x
        self.y = -self.y

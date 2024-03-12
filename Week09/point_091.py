#!/usr/bin/env python3

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def midpoint(self, other):
        x_m = (self.x + other.x) / 2
        y_m = (self.y + other.y) / 2
        return Point(x_m, y_m)
        
    def __str__(self):
        return f'({self.x:.01f}, {self.y:.01f})'

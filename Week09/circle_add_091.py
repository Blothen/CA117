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
    

class Circle:
    def __init__(self, c=None, r=1):
        if c is None:
            c = Point()
        self.centre = c
        self.radius = r

    def __add__(self, other):
        c = (self.centre.midpoint(other.centre))
        r = (self.radius + other.radius)
        return (Circle(c, r))

    def __str__(self):
        return f'Centre: {self.centre}\nRadius: {self.radius}'
    

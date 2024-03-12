#!/usr/bin/env python3

class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points
        
    def __str__(self):
        return '{:d} goal(s) and {:d} point(s)'.format(
            self.goals, self.points
        )

    def score_calc(self):
        return self.goals * 3 + self.points

    def __eq__(self, other):
        return self.score_calc() == other.score_calc()
    
    def __gt__(self, other):
        return self.score_calc() > other.score_calc()

    def __le__(self, other):
        return self.score_calc() <= other.score_calc()

#!/usr/bin/env python3

# Runner

class Triathlete:
    def __init__(self, name, id):
        self.name = name
        self.tid = id

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}'

class Triathlon:
    def __init__(self):
        self.athletes = {}

    def add(self, athlete):
        self.athletes[athlete.tid] = athlete
        return self

    def lookup(self, id):
        if id in self.athletes:
            return self.athletes[id]
        return None

    def remove(self, id):
        self.athletes.pop(id)
        return self

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)

    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()
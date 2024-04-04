#!/usr/bin/env python3

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


    def __str__(self):
        output = sorted([str(t) for t in self.athletes.values()])
        return "\n".join(output)


# Runner

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()
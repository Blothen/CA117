#!/usr/bin/env python3

class Triathlete:
    def __init__(self, name, id):
        self.name = name
        self.tid = id
        self.times = {}

    def add_time(self, activity, time):
        self.times[activity] = time

    def get_time(self, activity):
        return self.times[activity]

    def total_time(self, times=None):
        if times is None:
            times = self.times
        total = 0
        for k, v in times.items():
            total += v
        return total

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {self.total_time()}'

    def __eq__(self, other):
        return self.total_time() == self.total_time(other.times)

    def __lt__(self, other):
        return self.total_time() < self.total_time(other.times)

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

    def best(self):
        best = None
        for t in self.athletes.values():
            if best is None:
                best = t
            elif best > t:
                best = t
        return best

    def worst(self):
        worst = None
        for t in self.athletes.values():
            if worst is None:
                worst = t
            elif worst < t:
                worst = t
        return worst


    def __str__(self):
        output = sorted([str(t) for t in self.athletes.values()])
        return "\n".join(output)

# Runner


def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()
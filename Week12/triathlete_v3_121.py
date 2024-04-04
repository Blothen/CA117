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

# Runner


def main():

    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 150)
    t3.add_time('cycle', 120)
    t3.add_time('run', 100)

    print(t1)
    print(t2)
    print(t3)

    assert(t1 == t3)
    assert(t1 < t2)
    assert(t2 > t3)

if __name__ == '__main__':
    main()
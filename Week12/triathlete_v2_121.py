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

    def __str__(self):
        total = 0
        for k, v in self.times.items():
            total += v
        return f'Name: {self.name}\nID: {self.tid}\nRace time: {total}'

# Runner


def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()
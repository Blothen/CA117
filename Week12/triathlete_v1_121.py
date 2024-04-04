#!/usr/bin/env python3

class Triathlete:
    def __init__(self, name, id):
        self.name = name
        self.tid = id

    def __str__(self):
        return f'Name: {self.name}\nID: {self.tid}'

# Caller 

def main():
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    assert(t1.name == 'Ian Brown')
    assert(t1.tid == 21)

    print(t1)
    print(t2)

if __name__ == '__main__':
    main()
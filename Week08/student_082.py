#!/usr/bin/env python3

class Student:
    def __init__(self, sid, name, modlist=None):
        self.sid = sid
        self.name = name
        self.modlist = [] if modlist is None else modlist

    def __str__(self):
        modules= ', '.join(sorted(self.modlist))
        return f'ID: {self.sid}\nName: {self.name}\nModules: {modules}'

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)

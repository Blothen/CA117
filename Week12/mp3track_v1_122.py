#!/usr/bin/env python

class MP3Track:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def __str__(self):
        return f'Title: {self.title}\nDuration: {self.duration}'
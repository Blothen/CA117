#!/usr/bin/env python

class MP3Track:
    def __init__(self, title, duration, artists):
        self.title = title
        self.duration = duration
        self.artists = artists

    def __str__(self):
        artists_str = ', '.join(self.artists)
        mins = self.duration // 60
        secs = self.duration % 60
        return f'Title: {self.title}\nDuration: {mins}:{secs:02}\nBy: {artists_str}'



if __name__ == "__main__":
    t1 = MP3Track('Fools Gold', 604, ['The Stone Roses'])
    t2 = MP3Track('Shallow', 197, ['Lady Gaga', 'Bradley Cooper'])
    t3 = MP3Track('Telephone', 220, ['Beyonce', 'Lady Gaga'])
    t4 = MP3Track('Her Majesty', 34, ['The Beatles'])
    t5 = MP3Track('Seven Seconds', 7, ['Neneh Cherry'])

    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print(t5)
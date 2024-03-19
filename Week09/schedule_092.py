
class Meeting:
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        
    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'
    

class Schedule:
    def __init__(self):
        self.schedule = []
        
    def add(self, meeting):
        self.schedule.append(meeting)
        
    def __str__(self):
        output = 'Schedule\n--------\n'
        meetings = sorted([str(m) for m in self.schedule])
        return output + '\n'.join(meetings) + '\nMeetings today: ' + str(len(meetings))


def main():
    schedule = Schedule()

    m = Meeting(13, 0, 15)
    schedule.add(m)

    m = Meeting(9, 5, 30)
    schedule.add(m)

    m = Meeting(16, 30, 5)
    schedule.add(m)

    print(schedule)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
import sys

def parse_time(time_str):
    parts = time_str.split(':')
    if len(parts) != 2:
        return None
    try:
        minutes = int(parts[0])
        seconds = int(parts[1])
        if seconds < 0 or seconds >= 60 or minutes < 0:
            return None
        return minutes * 60 + seconds
    except ValueError:
        return None

best_time = float('inf')
best_runner = None

for line in sys.stdin:
    data = line.strip().split()
    runner_name = data[0]
    race_times = data[1:]

    valid_times = []
    for time_str in race_times:
        time = parse_time(time_str)
        if time is None:
            break
        valid_times.append(time)
    valid_times = [time for time in valid_times if time is not None]

    if valid_times:
        min_time = min(valid_times)
        if min_time < best_time:
            best_time = min_time
            best_runner = runner_name

if best_runner is not None:
    minutes = best_time // 60
    seconds = best_time % 60
    print(f"{best_runner} : {int(minutes)}:{seconds:02d}")

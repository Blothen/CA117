import sys


values = []


def trustworthy(log):
    for line in log:
        line = line.strip()
        if line == "correct":
            return "Bert can be trusted" if guessed_number is not None else "Berst is not to be trusted"
        elif line == "higher":
            if guessed_number is not None and guessed_number >= prev_guess:
                return "Bert is not to be trusted"
            prev_guess = guessed_number
            guessed_number = None
        elif line == "lower":
            if guessed_number is not None and guessed_number <= prev_guess:
                return "Bert is not to be trusted"
            prev_guess = guessed_number
            guessed_number = None
        else:
            guessed_number = int(line)


for item in sys.stdin:
    values.append(item)

print(values)
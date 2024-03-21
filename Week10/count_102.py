
def count(s, c=0):
    if s == "":
        return c
    return count(s[1:], c + 1)


def main():
    print(count('cat'))
    print(count('catastrophe'))
    print(count(''))

if __name__ == '__main__':
    main()
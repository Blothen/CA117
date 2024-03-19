import sys

def matcher(string):
    brackets = {
        "{": 0,
        "}": 0,
        "(": 0,
        ")": 0,
        "[": 0,
        "]": 0
    }
    for line in string:
        if line in brackets:
            brackets[line] += 1
        
    if brackets['('] != brackets[')']:
        return False
    elif brackets['['] != brackets[']']:
        return False
    elif brackets['{'] != brackets['}']:
        return False
    return True

tests = ['()',
'(())',
'(({}))',
'(())(){}{(([]))}',
'(()',
'(()){()]',
')(()){([()])}']

def main():

    for test in tests:
        print(matcher(test.strip()))

if __name__ == '__main__':
    main()

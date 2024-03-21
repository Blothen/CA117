
def biggest(l, bigvalue=None):
    if bigvalue == None:
        bigvalue = l[0]
    for item in l:
        if item > bigvalue:
            return biggest(l, item)
    return bigvalue

def main():
    print(biggest([6,5,1,3,4]))
    print(biggest([6,5,11,3,4]))
    print(biggest([6,15,11,13,14]))
    print(biggest([6,15,11,13,4]))

if __name__ == '__main__':
    main()
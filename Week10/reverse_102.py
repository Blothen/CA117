
def reverse(l, nl=None, length=None):
    nl = nl if nl is not None else []
    if length == None:
        length = len(l)
    if len(nl) == length or l == []:
        return nl
    nl.append(l[-1])
    return reverse(l[:-1], nl, length)

def main():
    print(reverse([1,2,3]))
    print(reverse([3,4,5,6]))
    print(reverse([1,2]))

if __name__ == '__main__':
    main()
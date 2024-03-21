
def sumup(n, total=0):
    return total if n == 0 else sumup(n - 1, total + n)

def main():
    print(sumup(0))
    print(sumup(1))
    print(sumup(12))

if __name__ == '__main__':
    main()
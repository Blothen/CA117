
def factorial(n, total=1):
    if n == 0:
        return total
    total = total * n
    return factorial(n - 1, total)

def main():
    print(factorial(0))
    print(factorial(1))
    print(factorial(12))

if __name__ == '__main__':
    main()
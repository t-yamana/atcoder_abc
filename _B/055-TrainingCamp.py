from math import factorial

if __name__ == '__main__':
    n = int(input())
    print(factorial(n) % 1_000_000_007)

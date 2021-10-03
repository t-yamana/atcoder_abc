
from math import sqrt

if __name__ == '__main__':
    n = int(input())

    combs = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            assert(n/i == int(n/i))
            # .00 すらも後に続かないように整数除算(//)する
            # str(3.00) -> '3.0'
            combs.append(max(len(str(i)), len(str(n//i))))

    print(min(combs))

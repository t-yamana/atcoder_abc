
if __name__ == '__main__':
    # 10進数n を k進数 へ変化
    n, k = map(int, input().split())
    digi = ''

    while n != 0:
        digi = str(n % k) + digi
        n = n // k

    print(len(digi))

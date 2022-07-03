
if __name__ == '__main__':
    n, y = map(int, input().split())

    ichim = y // 10_000

    for i in range(ichim + 1):
        for j in range(n-i+1):
            money = 10_000 * i + 5_000 * j + 1_000 * (n-i-j)
            if money == y:
                print(i, j, n-i-j)
                exit()
    print(-1, -1, -1)

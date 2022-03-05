# https://atcoder.jp/contests/abc241/tasks/abc241_c

def char2num(x):
    return ".#".index(x)


# 6 <= n <= 1000 のとき
# 6 * {2n(n-5) + 2(n-5)^2} < 24n^2
if __name__ == "__main__":
    n = int(input())

    mtx = [list(map(char2num, input())) for _ in range(n)]
    for r in range(n-5):
        for c in range(n):
            cnt = sum([mtx[r+i][c] for i in range(6)])
            if cnt >= 4:
                print("Yes")
                exit()
    for r in range(n):
        for c in range(n-5):
            cnt = sum([mtx[r][c+i] for i in range(6)])
            if cnt >= 4:
                print("Yes")
                exit()
    for r in range(n-5):
        for c in range(n-5):
            cnt = sum([mtx[r+i][c+i] for i in range(6)])
            if cnt >= 4:
                print("Yes")
                exit()
    for r in range(0, n-5):
        for c in range(5, n):
            cnt = sum([mtx[r+i][c-i] for i in range(6)])
            if cnt >= 4:
                print("Yes")
                exit()

    print("No")

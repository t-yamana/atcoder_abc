# https://atcoder.jp/contests/abc161/tasks/abc161_d

from collections import deque

if __name__ == '__main__':
    n = int(input())

    Q = deque()
    Q.extend([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 複数プッシュ

    cnt = 0
    while len(Q) > 0:
        a = Q.popleft()

        cnt += 1
        if cnt == n:
            print(a)
            exit()

        x = a % 10  # 一の位の数字
        for xi in [x-1, x, x+1]:
            if 0 <= xi <= 9:
                Q.append(a * 10 + xi)

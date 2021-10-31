# https://atcoder.jp/contests/abc114/tasks/abc114_c

from collections import deque
from copy import deepcopy

if __name__ == '__main__':
    n = int(input())

    Q = deque()
    Q.append((0, False, False, False))

    cnt = 0
    while len(Q) > 0:
        tup = Q.popleft()

        flg = [tup[1], tup[2], tup[3]]

        if flg[0] and flg[1] and flg[2]:
            cnt += 1

        for idx, xi in enumerate([3, 5, 7]):
            calc = tup[0] * 10 + xi
            if calc <= n:
                new_flg = deepcopy(flg)
                new_flg[idx] = True
                Q.append((calc, *new_flg))

    print(cnt)

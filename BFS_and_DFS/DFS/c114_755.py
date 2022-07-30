# https://atcoder.jp/contests/abc114/tasks/abc114_c

import sys
from copy import deepcopy
sys.setrecursionlimit(1_000_000)

if __name__ == '__main__':
    maxim = int(input())
    cnt = 0

    def dfs(x: int, cmb: set) -> None:
        global cnt
        if len(cmb) == 3:
            cnt += 1
        for y in [3, 5, 7]:
            calc = 10*x + y
            if calc <= maxim:
                new_s = deepcopy(cmb)
                new_s.add(y)
                dfs(x*10+y, new_s)

    dfs(0, set())
    print(cnt)

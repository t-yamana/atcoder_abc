# https://atcoder.jp/contests/atc001/tasks/dfs_a

import sys
sys.setrecursionlimit(1_000_000)

if __name__ == '__main__':
    h, w = map(int, input().split())

    cells = [None] * h
    visited = [[False] * w for _ in range(h)]
    start = None
    goal = None

    for i in range(h):
        row = input()
        cells[i] = row

        s_x = row.find('s')
        if s_x != -1:
            start = (i, s_x)
        g_x = row.find('g')
        if g_x != -1:
            goal = (i, g_x)

    def dfs(i: int, j: int) -> None:
        visited[i][j] = True
        for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= y < h and 0 <= x < w):
                continue
            if not visited[y][x] and cells[y][x] != '#':
                dfs(y, x)

    dfs(start[0], start[1])
    print('Yes' if visited[goal[0]][goal[1]] else 'No')

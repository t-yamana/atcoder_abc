# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

if __name__ == '__main__':
    r, c = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())

    sy, sx, gy, gx = map(lambda x: x-1, [sy, sx, gy, gx])

    s = [None] * r
    for i in range(r):
        s[i] = input()

    # 掛け算を使用する場合は、変更できないオブジェクト(Noneなど)である必要がある
    # [None, ...] のリストは変更可能なので注意
    costs = [[-1] * c for _ in range(r)]

    Q = deque()
    Q.append((sy, sx))
    costs[sy][sx] = 0

    while len(Q) > 0:
        i, j = Q.popleft()
        for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= y < r and 0 <= x < c):
                continue
            if s[y][x] == '#':
                continue
            if costs[y][x] == 0:
                costs[y][x] = costs[i][j] + 1
                Q.append((y, x))

    print(costs[gy][gx])

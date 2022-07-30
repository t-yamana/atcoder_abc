# https://atcoder.jp/contests/past202005-open/tasks/past202005_g

from collections import deque

if __name__ == '__main__':
    n, g_x, g_y = map(int, input().split())

    # 障害物と既チェックを合わせて無視座標リスト
    neg = set()
    for _ in range(n):
        xi, yi = map(int, input().split())
        neg.add((xi, yi))

    Q = deque()
    neg.add((0, 0))
    Q.append(((0, 0), 0))

    # ゴールまで到達可能な経路が存在しない場合もある
    reached = False

    while len(Q) > 0:
        (i, j), d = Q.popleft()
        if (i, j) == (g_x, g_y):
            reached = True
            break
        for x, y in [
            (i+1, j+1), (i,   j+1), (i-1, j+1),
            (i+1, j), (i-1, j), (i, j-1)
        ]:
            # ゴール座標・障害物は境界があるが、経路には限界がないので回り込める
            if not (-201 <= x <= 201 and -201 <= y <= 201):
                continue
            if (x, y) in neg:
                continue
            neg.add((x, y))
            Q.append(((x, y), d+1))

    if reached:
        print(d)
    else:
        print(-1)

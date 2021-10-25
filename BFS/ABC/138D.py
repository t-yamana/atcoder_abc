# https://atcoder.jp/contests/abc138/tasks/abc138_d

from collections import deque

if __name__ == '__main__':
    n, q = map(int, input().split())

    edges = [[] for _ in range(n)]
    points = [0] * n
    visited = [False] * n

    for _ in range(n-1):
        frm, to = map(int, input().split())
        edges[frm-1].append(to-1)
        edges[to-1].append(frm-1)  # 逆方向の連結リスト

    for _ in range(q):
        no, val = map(int, input().split())
        points[no-1] += val

    Q = deque()
    Q.append((0, 0))
    while len(Q) > 0:
        no, st_pt = Q.popleft()  # stack_point
        if not visited[no]:
            # 訪問済みチェックを取り出し後にするパターンで書いている
            # エンキュー時チェックだと下記のようにまとめて入れられない
            visited[no] = True

            points[no] += st_pt
            # リストとして複数アイテムを一度にプッシュ
            Q.extend([(n, points[no]) for n in edges[no]])

    print(*points)  # 改行区切りではなく空白区切りで出力

# https://atcoder.jp/contests/abc204/tasks/abc204_c

from collections import deque

if __name__ == '__main__':
    n, m = map(int, input().split())

    connection = [[] for _ in range(n)]
    for i in range(m):
        frm, to = map(int, input().split())
        connection[frm-1].append(to-1)

    trip = 0

    # Aパターン: デキュー後に訪問済みチェックする書き方
    # Bパターン: エンキュー前に訪問済みチェックする書き方

    for idx in range(n):
        visited = [False] * n

        Q = deque()
        # visited[idx] = True  # Bパターンのみ
        Q.append(idx)

        while len(Q) > 0:
            ci = Q.popleft()  # city_id

            # Aパターンのみ
            if visited[ci]:
                continue
            else:
                trip += 1
                visited[ci] = True

            for to_c in connection[ci]:
                if not visited[to_c]:

                    # Bパターン
                    # trip += 1
                    # visited[to_c] = True

                    Q.append(to_c)

    print(trip)

# https://atcoder.jp/contests/abc158/tasks/abc158_d

from collections import deque

if __name__ == '__main__':
    txt = input()

    Q = deque()
    Q.extend(txt)  # iterable をまとめてエンキュー

    flipped = False

    q = int(input())
    for _ in range(q):
        di = ''.join(input().split())  # directive

        if di[0] == '1':
            flipped = not flipped
        else:
            if di[1] == '1':
                if flipped:
                    Q.append(di[2])
                else:
                    Q.appendleft(di[2])
            elif di[1] == '2':
                if flipped:
                    Q.appendleft(di[2])
                else:
                    Q.append(di[2])

    txt = ''.join(Q)
    if flipped:
        txt = txt[::-1]

    print(txt)

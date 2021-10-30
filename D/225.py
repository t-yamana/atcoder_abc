
if __name__ == '__main__':
    n, q = map(int, input().split())

    prev = [None] * n
    next = [None] * n

    direcs = [None] * q
    for i in range(q):
        direc = list(map(int, input().split()))
        direc = list(map(lambda x: x-1, direc))
        direcs[i] = direc

    for i in range(q):
        direc = direcs[i]
        if direc[0] == 0:
            x, y = direc[1], direc[2]
            next[x] = y
            prev[y] = x
        elif direc[0] == 1:
            x, y = direc[1], direc[2]
            next[x] = None
            prev[y] = None
        else:
            x = direc[1]
            pv = prev[x] or x  # None になるぐらいなら x
            while prev[pv] is not None:
                pv = prev[pv]
            train = []
            nx = pv
            train.append(nx+1)
            while next[nx] is not None:
                nx = next[nx]
                train.append(nx+1)
            print(len(train), end=' ')
            [print(a, end=' ') for a in train]
            print()


if __name__ == '__main__':
    h, w = map(int, input().split())

    mtx = [[None] * w for _ in range(h)]

    for i in range(h):
        mtx[i] = list(map(int, input().split()))

    for i1 in range(h):
        for i2 in range(i1, h):
            for j1 in range(w):
                for j2 in range(j1, w):
                    if mtx[i1][j1] + mtx[i2][j2] > mtx[i1][j2] + mtx[i2][j1]:
                        print('No')
                        exit()

    print('Yes')


if __name__ == '__main__':
    h, w = map(int, input().split())
    cells = [[None] * w] * h

    for i in range(h):
        cells[i] = [c for c in input()]

    cells.insert(0,   ['.'] * w)
    cells.insert(h+1, ['.'] * w)

    for i in range(h+2):
        cells[i].insert(0,   '.')
        cells[i].insert(w+1, '.')

    # for i in range(h+2):
    #     print(cells[i])

    be_able = True
    for i in range(h+2):
        for j in range(w+2):
            if cells[i][j] == '#':
                check_arr = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]

                is_ok = False
                for ch in check_arr:
                    if cells[ch[0]][ch[1]] == '#':
                        is_ok = True
                        break
                if not is_ok:
                    print('No')
                    exit()

    print('Yes')

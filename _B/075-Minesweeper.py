
if __name__ == '__main__':
    h, w = map(int, input().split())
    cells = [[None] * w] * h

    for i in range(h):
        cells[i] = [c for c in input()]

    for i in range(h):
        for j in range(w):
            if cells[i][j] == '.':
                cells[i][j] = 0

    cells.insert(0, [0] * w)
    cells.insert(h+1, [0] * w)

    for i in range(h+2):
        cells[i].insert(0, 0)
        cells[i].insert(w+1, 0)

    for i in range(h+2):
        for j in range(w+2):
            if cells[i][j] == '#':
                for y in range(i-1, i+2):
                    for x in range(j-1, j+2):
                        if cells[y][x] != '#':
                            cells[y][x] += 1

    for i in range(1, h+1):
        print(''.join(map(str, cells[i][1:w+1:1])))

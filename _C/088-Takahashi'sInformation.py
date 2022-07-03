
if __name__ == '__main__':
    c11, c12, c13 = map(int, input().split())
    c21, c22, c23 = map(int, input().split())
    c31, c32, c33 = map(int, input().split())

    cells = [[c11, c12, c13], [c21, c22, c23], [c31, c32, c33]]

    for x in range(2):
        delta_x = cells[0][x] - cells[0][x+1]
        for y in range(1, 3):
            # print((y, x), '=', (y, x+1))
            if cells[y][x] - cells[y][x+1] != delta_x:
                print('No')
                exit()

    print('Yes')


from typing import List


def rotate(arr: List[int], limit: int) -> List[int]:
    new_arr = [None] * len(arr)
    for i in range(len(arr)):
        cell = arr[i]
        new_arr[i] = [cell[1], (limit - 1) - cell[0]]
    return new_arr


def cell_lists(limit: int) -> List[int]:
    cells = []
    for i in range(limit):
        row = input()
        for j in range(limit):
            if row[j] == '#':
                cells.append([i, j])
    return cells


def is_pararells(s_cells: List[int], t_cells: List[int]) -> bool:
    min_x = float('inf')
    min_y = float('inf')
    for cell in s_cells:
        if cell[0] < min_x:
            min_x = cell[0]
        if cell[1] < min_y:
            min_y = cell[1]
    sp_cells = []
    for a in s_cells:
        sp_cells.append((a[0] - min_x, a[1] - min_y))

    min_x = float('inf')
    min_y = float('inf')
    for cell in t_cells:
        if cell[0] < min_x:
            min_x = cell[0]
        if cell[1] < min_y:
            min_y = cell[1]

    tp_cells = []
    for a in t_cells:
        tp_cells.append((a[0] - min_x, a[1] - min_y))

    # それぞれがタプルの配列じゃないと集合にキャスト出来なかった
    # X: [[1, 2], [2, 3]]
    # O: [(1, 2), (2, 3)]
    if set(sp_cells) == set(tp_cells):
        return True
    else:
        return False


if __name__ == '__main__':
    limit = int(input())
    s_cells = cell_lists(limit)
    t_cells = cell_lists(limit)

    is_same = False
    is_same = is_pararells(s_cells, t_cells)

    for _ in range(3):
        if is_same:
            break
        t_cells = rotate(t_cells, limit)
        is_same = is_pararells(s_cells, t_cells)

    print('Yes') if is_same else print('No')

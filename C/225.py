
if __name__ == '__main__':
    n, m = map(int, input().split())

    is_rec = True

    row = list(map(int, input().split()))
    for idx in range(m-1):
        if row[idx] % 7 == 0:
            is_rec = False

    cur = row[0]
    for idx in range(1, m):
        if row[idx] - cur != 1:
            is_rec = False
        cur = row[idx]

    lp = 1

    def shu(lp, arr):
        delta = lp * 7
        return list(map(lambda x: x + delta, arr))

    for i in range(n-1):
        obj_row = shu(lp, row)  # ほしい行
        nxt_row = list(map(int, input().split()))
        if obj_row != nxt_row:
            is_rec = False
        lp += 1

    print('Yes') if is_rec else print('No')

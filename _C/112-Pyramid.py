
from sys import stdin

if __name__ == '__main__':
    n = int(input())

    coods = [None] * n
    for i in range(n):
        # 複数行のインプットには stdin.readline() を使用しないと遅くなる
        coods[i] = list(map(int, stdin.readline().split()))

    high_cood = None
    highest = 0
    for cood in coods:
        if cood[2] > highest:
            highest = cood[2]
            high_cood = cood
    # 現状の最も高い点を高度計算に使用する
    assert(high_cood is not None)

    # 背理法で探索する
    for i in range(101):
        for j in range(101):
            delta_x = abs(high_cood[0] - i)
            delta_y = abs(high_cood[1] - j)
            # 最高点だと仮定して計算された高度
            pseudo_h = high_cood[2] + delta_x + delta_y
            flag = True

            # 他の点に対して矛盾しないかチェックする
            for cood in coods:
                delta_x = abs(cood[0] - i)
                delta_y = abs(cood[1] - j)
                # 平地(0)の場合を忘れない
                if cood[2] != max(pseudo_h - delta_x - delta_y, 0):
                    flag = False
                    break

            if flag is False:
                continue
            else:  # 全ての点で矛盾が出なかった
                print(i, j, pseudo_h)
                exit()

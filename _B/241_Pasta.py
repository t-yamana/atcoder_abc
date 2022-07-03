# https://atcoder.jp/contests/abc241/tasks/abc241_b

# 重複アリの部分集合になっているかチェックする
if __name__ == "__main__":
    n, m = map(int, input().split())
    udons = list(map(int, input().split()))
    udons.sort()
    plans = list(map(int, input().split()))
    plans.sort()

    i = 0
    for day in range(m):
        obj = plans[day]
        while udons[i] < obj and i+1 < n:
            i = i+1
        if udons[i] > obj:
            # 見つからなかった(越した)
            print('No')
            exit()
        elif udons[i] < obj:
            # 最後尾なのに短かった
            print('No')
            exit()
        elif i+1 == n and day+1 < m:
            # 最後尾で見つかったが最終日でなかった
            print('No')
            exit()
        elif i+1 < n:
            # 見つかったので次へ行く
            i = i+1  # 同じのは使えないから

    print("Yes")

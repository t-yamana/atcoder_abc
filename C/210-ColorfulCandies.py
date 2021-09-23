from collections import Counter

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    counter = Counter()
    ans = 0
    types = 0

    # ヒストグラムを移動更新するループ
    for i in range(n):
        counter[arr[i]] += 1

        if counter[arr[i]] == 1:
            # エリアに新しく入ってきた要素がユニークだった時
            types += 1

        if i-k >= 0:
            # エリアから外れる要素がある時
            lost = arr[i-k]
            counter[lost] -= 1
            if counter[lost] == 0:
                # 外れた要素がユニークだった場合
                types -= 1

        ans = max(ans, types)
    print(ans)

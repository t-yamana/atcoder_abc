import itertools

if __name__ == '__main__':
    num = int(input())

    secs = list(map(int, input().split()))
    timings = list(map(int, input().split()))

    data = [None] * num
    for i in range(num):
        data[i] = [secs[i], timings[i]]
    data_itr = itertools.cycle(data)

    tmp = float('inf')
    for (idx, elm) in enumerate(data_itr):
        # 廻ってくるのを待つのが早いか、直接貰うのが早いか
        elm[1] = min(tmp, elm[1])
        tmp = elm[1] + elm[0]

        # 終了条件(ちょうど二周ループしないところまでループさせる)
        # 最初の要素に一周後に更新が掛かった場合もう一周必要なので
        if idx == 2 * num - 1:
            break

    # 内部的な next() の実行回数を引き継いでいる
    for (idx, elm) in enumerate(data_itr):
        # 終了条件
        if idx == num:
            break

        print(elm[1])

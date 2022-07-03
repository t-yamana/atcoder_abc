
if __name__ == '__main__':
    _, k = map(int, input().split())
    balls = list(map(int, input().split()))

    ball_cnt = {}
    for b in balls:
        ball_cnt.setdefault(b, 0)
        ball_cnt[b] += 1

    nums_cnt = [[k, v] for k, v in ball_cnt.items()]
    nums_cnt = sorted(nums_cnt, key=lambda tup: tup[1], reverse=True)

    # 以下は TLE
    # write_time = 0
    # while len(nums_cnt) > k:
    #     write_time += nums_cnt[0][1]
    #     nums_cnt.pop(0)  # 先頭要素の削除

    k = min(len(nums_cnt), k)  # より小さいほうで更新
    for i in range(k):
        nums_cnt.pop(0)  # 絞る数を先に抜き出す

    # 残りは全て上書き回数になるので走査で合計
    write_time = 0
    for li in nums_cnt:
        write_time += li[1]

    print(write_time)

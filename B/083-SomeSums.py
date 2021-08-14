
if __name__ == '__main__':
    n, a, b = map(int, input().split())
    sum = 0
    for i in range(n+1):
        i_org = i
        tmp_sum = 0

        # tmp_sum += i // 10000
        # i = i % 10000
        # tmp_sum += i // 1000
        # i = i % 1000
        # tmp_sum += i // 100
        # i = i % 100
        # tmp_sum += i // 10
        # i = i % 10
        # tmp_sum += i // 1

        # 上と同じ処理が以下で書ける
        while i > 0:
            tmp_sum += i % 10
            i = i // 10

        if a <= tmp_sum and tmp_sum <= b:
            sum += i_org
    print(sum)

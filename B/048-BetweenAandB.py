
if __name__ == '__main__':
    a, b, x = map(int, input().split())
    cnt = 0

    if a % x == 0:
        cnt += 1

    # cnt += (b-a)//x
    # ▲コッチだとダメ
    cnt += (b//x) - (a//x)

    print(cnt)

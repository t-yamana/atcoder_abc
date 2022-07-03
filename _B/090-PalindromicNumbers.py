
if __name__ == '__main__':
    a, b = map(int, input().split())
    cnt = 0

    for i in range(a, b+1, 1):
        if str(i)[::-1] == str(i):
            cnt += 1

    print(cnt)

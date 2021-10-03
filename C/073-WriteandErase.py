

if __name__ == '__main__':
    n = int(input())

    hist = {}
    for _ in range(n):
        ch = input()
        hist.setdefault(ch, 0)
        hist[ch] += 1

    cnt = 0
    for it in hist.values():
        if it % 2 == 1:
            cnt += 1

    print(cnt)

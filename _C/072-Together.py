
if __name__ == '__main__':
    _ = int(input())
    arr = list(map(int, input().split()))

    hist = {}
    for a in arr:
        hist.setdefault(a, 0)
        hist[a] += 1

    maxas = 0
    max_key = None
    for i in range(max(arr)+1):
        amt = 0
        for ext in range(i, i+3):
            try:
                amt += hist[ext]
            except KeyError:
                continue
        if amt > maxas:
            maxas = amt
            max_key = i

    print(maxas)

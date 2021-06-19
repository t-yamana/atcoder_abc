
n = int(input())
arr = [int(a) for a in input().split()]
hist = {}
for a in arr:
    value = hist.setdefault(a, 0)  # key が未登録の時 0 で登録後取得
    hist[a] = value + 1

total = n
ans = 0
for v in hist.values():
    total -= v
    ans += v * total
print(ans)

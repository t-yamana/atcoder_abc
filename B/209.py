
n, x = map(int, input().split())
arr = map(int, input().split())

total = 0
for i, a in enumerate(arr):
    if i % 2 == 0:
        total += a
    else:
        total += a-1

print('Yes' if total <= x else 'No')

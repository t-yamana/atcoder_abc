
input()  # 使わないので代入しない
arr = [int(a) for a in input().split()]

min = arr[0]
max = arr[0]

for a in arr:
    if a < min:
        min = a
    elif max < a:
        max = a

print(max-min)
# print(max(arr) - min(arr))

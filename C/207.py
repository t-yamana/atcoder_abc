
n = int(input())
span_arr = [None] * n
for i in range(n):
    t, le, r = (int(a) for a in input().split())
    if t == 2:
        r -= 0.1
    elif t == 3:
        le += 0.1
    elif t == 4:
        r -= 0.1
        le += 0.1
    span_arr[i] = (le, r)

cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        start_i = span_arr[i][0]
        end_i = span_arr[i][1]
        start_j = span_arr[j][0]
        end_j = span_arr[j][1]
        # この一行だけでチェックできるのがポイント
        if max(start_i, start_j) <= min(end_i, end_j):
            cnt += 1

print(cnt)

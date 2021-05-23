
num = int(input())
arr_a = [int(a) for a in input().split()]
arr_b = [int(a) for a in input().split()]
arr_c = [int(a) for a in input().split()]

cnt_hist = [0] * num
for a in arr_a:
    cnt_hist[a-1] += 1

cnt = 0
for i in arr_c:
    cnt += cnt_hist[arr_b[i-1]-1]
print(cnt)


import math

_ = input()
arr = [int(n) for n in input().split()]

# 0 ~ 199 の度数分布表
hist = [0] * 200
for n in arr:
    hist[n % 200] += 1

# 2 以上でカウント発生
cnt = 0
filtered_hist = [a for a in hist if a > 1]
for i in filtered_hist:
    # 組み合わせ数を加算
    cnt += math.factorial(i) // (math.factorial(i-2) * 2)

print(cnt)

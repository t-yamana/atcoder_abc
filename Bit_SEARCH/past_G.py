# https://atcoder.jp/contests/past201912-open/tasks/past201912_g

n = int(input())

happy = [None] * (n-1)  # 最後の人のデータは省略
for i in range(n-1):
  dt = list(map(int, input().split()))
  dt = [0] * (n - len(dt)) + dt
  happy[i] = dt

def sum_happy(a: int) -> int:
  total = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if a & (1<<i) and a & (1<<j):
        total += happy[i][j]
  return total

# 問題の条件から求まる最悪のケース
ans = -1 * 1_000_000 * (10*10)

all = 1<<n
for s1 in range(all):
  for s2 in range(all):
    if s1&s2:
      continue
    s3 = all-1 - (s1|s2)
    ans = max(ans, sum_happy(s1) + sum_happy(s2) + sum_happy(s3))
print(ans)

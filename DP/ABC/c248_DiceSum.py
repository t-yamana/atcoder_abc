# https://atcoder.jp/contests/abc248/tasks/abc248_c

n, m, k = map(int, input().split())

# dp[amount][idx]
dp = [[0] * (n+1) for _ in range(k+1)]  # (0~N, 0~K)

dp[0][0] = 1  # []

for amt in range(k+1):
  for idx in range(n):
    if dp[amt][idx] == 0: continue

    for nxt in range(1, m+1):
      if (amt+nxt) <= k:
        dp[amt+nxt][idx+1] += dp[amt][idx]

amount = 0
for i in range(k+1):
  amount += dp[i][n]

print(amount % 998_244_353)

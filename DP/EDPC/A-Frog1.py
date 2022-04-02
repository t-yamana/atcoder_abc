# https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
steps = list(map(int, input().split())) + [0]

dp = [None] * (n+1)
dp[0] = 0

for i in range(0, n-1):
  calc_1 = dp[i] + abs(steps[i]-steps[i+1])
  dp[i+1] = calc_1 if dp[i+1] is None else min(calc_1, dp[i+1])

  calc_2 = dp[i] + abs(steps[i]-steps[i+2])
  dp[i+2] = calc_2 if dp[i+2] is None else min(calc_2, dp[i+2])

print(dp[n-1])  # n番目

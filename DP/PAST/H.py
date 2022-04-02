# https://atcoder.jp/contests/past202005-open/tasks/past202005_h

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, l = LI()
obs = LI()
t1, t2, t3 = LI()

H = [False] * (l+1)
for o in obs:
  H[o] = True

dp = [float('inf')] * (l+1)
dp[0] = 0

for i in range(1, l+1):
  dp[i] = min(dp[i], dp[i-1] + t1)
  if i > 1:
    dp[i] = min(dp[i], dp[i-2] + t1 + t2)
  if i > 3:
    dp[i] = min(dp[i], dp[i-4] + t1 + 3*t2)

  if H[i]:
    dp[i] += t3

ans = dp[l]

# jumpable reach
for j in [l-3, l-2, l-1]:
  if j >= 0:
    # 出力時に少数にならないように注意する
    ans = min(ans, dp[j] + t1//2 + int(t2*(l-j-0.5)))

print(ans)

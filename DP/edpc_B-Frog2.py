# https://atcoder.jp/contests/dp/tasks/dp_b

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, k = map(int, input().split())
steps = LI()

dp = [None] * n
dp[0] = 0
dp[1] = abs(steps[1]-steps[0])

for i in range(2, n):
  min_cost = float('inf')
  for j in range(i-k, i, 1):
    if j < 0: continue
    min_cost = min(min_cost, dp[j] + abs(steps[j]-steps[i]))
  dp[i] = min_cost

print(dp[n-1])

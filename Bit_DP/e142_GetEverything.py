# https://atcoder.jp/contests/abc142/tasks/abc142_e
# past_I.py とほぼ同じ

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, m = MI()

costs = [None] * m
keys = [None] * m

for i in range(m):
  costs[i], _ = MI()
  bit = 0
  for j in LI():
    bit = bit | 1 << (n-j)  # 1010
  keys[i] = bit

dp = [[None] * (1<<n) for _ in range(m+1)]
dp[0][0] = 0

for i in range(m):
  for idx, c in enumerate(dp[i]):
    if c is not None:
      next = dp[i+1]
      # pattern 1
      nidx = idx | keys[i]
      next[nidx] = min(c+costs[i], float('inf') if next[nidx] is None else next[nidx])
      # pattern 2
      next[idx] = min(c, float('inf') if next[idx] is None else next[idx])

if dp[m][(1<<n)-1] is None:
  print(-1)
  exit()
else:
  print(dp[m][(1<<n)-1])

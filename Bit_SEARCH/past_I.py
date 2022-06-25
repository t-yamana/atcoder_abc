# https://atcoder.jp/contests/past201912-open/tasks/past201912_i

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from functools import reduce

n, m = MI()
cmb = [None] * m
costs = [None] * m

def txt2bit(txt) -> int:
  bit = 0
  for idx, c in enumerate(list(txt)):
    if c == 'Y':
      bit = bit | 1 << (len(txt)-1-idx)
  return bit

for i in range(m):
  # ★ 違う型の受け取り方
  (txt, cost) = (lambda ipt: (ipt[0], int(ipt[1])))(input().split())
  cmb[i] = txt2bit(txt)
  costs[i] = cost

# 最低条件の確認
all_cmb = reduce(lambda c1,c2: c1|c2, cmb)
if bin(all_cmb) != "0b" + "1" * n:
  print(-1)
  exit()

# ★ 集合(1111) を数字としてインデックスに使用
# ★ n が小さいことを要確認
dp = [[None] * (1<<n) for _ in range(m+1)]
dp[0][0] = 0

for i in range(m):
  for idx, c in enumerate(dp[i]):
    if c is not None:
      next = dp[i+1]
      # pattern 1
      nidx = idx | cmb[i]
      next[nidx] = min(c+costs[i], float('inf') if next[nidx] is None else next[nidx])
      # pattern 2
      next[idx] = min(c, float('inf') if next[idx] is None else next[idx])

# ★ dpテーブルの最後のマスが答え
print(dp[m][(1<<n)-1])

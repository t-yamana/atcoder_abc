# https://atcoder.jp/contests/abc167/tasks/abc167_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from functools import reduce

bk, m, x = MI()

c = [None] * bk
learns = [None] * bk

for i in range(bk):
  c[i], *learn = MI()
  learns[i] = list(learn)

# 全ての本を使用しても足りない場合の除外
scores = [0] * m
for l in learns:
  for idx, s in enumerate(l):
    scores[idx] += s

test = list(filter(lambda s: s<x, scores))
if len(test) > 0:
  print(-1)
  exit()

# 全ての本を買った時の金額をベースに開始する
ans = reduce(lambda a,b: a+b, c)

for i in range(1 << bk):  # 2^bk
  # 「学習量」の Bit全探索
  scores = [0] * m
  for j in range(bk):
    if i & (1<<j):
      for idx, s in enumerate(learns[j]):
        scores[idx] += s
  test = list(filter(lambda s: s<x, scores))

  # 「金額」の Bit全探索
  if test == []:
    cost = 0
    for j in range(bk):
      if i & (1<<j):
        cost += c[j]
    ans = min(ans, cost)

print(ans)

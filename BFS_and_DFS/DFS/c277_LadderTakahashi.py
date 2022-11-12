# https://atcoder.jp/contests/abc277/tasks/abc277_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def TI(): return tuple(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import defaultdict
sys.setrecursionlimit(1_000_000)

n = I()
stairs = defaultdict(lambda: [])

for _ in range(n):
  a, b = MI()
  stairs[a].append(b)
  stairs[b].append(a)

# 速度改善のためにしたこと
# stairs 作成に bisect.insort_right は不要
# next in seen をリストではなく辞書にした

seen = defaultdict(int)
floors = {1}

def dfs(now: int) -> None:
  if seen[now]:
    return
  seen[now] = 1

  floors.add(now)
  for next in stairs[now]:
    dfs(next)

if (1 in stairs.keys()):
  dfs(1)

print(max(floors))

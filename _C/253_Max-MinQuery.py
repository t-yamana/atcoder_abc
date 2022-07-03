# https://atcoder.jp/contests/abc253/tasks/abc253_c

import sys, heapq
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

q = I()
S = dict()  # defaultdict(int) を使うとコード量が減る
mx = []
mn = []

for _ in range(q):
  query = LI()
  if len(query) == 1:
    while S.get(-mx[0], 0) == 0:
      heapq.heappop(mx)
    while S.get(mn[0], 0) == 0:
      heapq.heappop(mn)
    print(-mx[0] - mn[0])

  elif len(query) == 2:
    heapq.heappush(mx, -query[1])
    heapq.heappush(mn, query[1])

    cnt = S.get(query[1], 0)
    S[query[1]] = cnt+1

  elif len(query) == 3:
    cnt = S.get(query[1], 0)  # 存在しない検索もある
    lost = min(cnt, query[2])
    if lost == cnt:  # キーの削除が必要
      S.pop(query[1], None)  # pop は存在しないキーにも対応
    else:
      S[query[1]] = cnt - lost

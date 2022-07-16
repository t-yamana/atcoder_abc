# https://atcoder.jp/contests/abc181/tasks/abc181_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
pts = [LI() for _ in range(n)]

def is_inline(i, j, k) -> bool:
  x1, y1 = i[0], i[1]
  x2, y2 = j[0], j[1]
  x3, y3 = k[0], k[1]
  left = (y3-y1) * (x2-x1)
  right = (y2-y1) * (x3-x1)
  return left == right

for i in range(0, n-2):
  for j in range(i+1, n-1):
    for k in range(j+1, n):
      if is_inline(pts[i], pts[j], pts[k]):
        print('Yes')
        exit()
print('No')

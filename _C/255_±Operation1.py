# https://atcoder.jp/contests/abc255/tasks/abc255_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

x, a, d, n = MI()
v1 = a
v2 = a + d * (n-1)
mn = min(v1, v2)
mx = max(v1, v2)

if x <= mn:
  print(mn - x)
  exit()
elif mx <= x:
  print(x - mx)
  exit()

modulo = abs((x-a) % d)  # マイナスもある
if modulo <= abs(d) - modulo:
  print(modulo)
else:
  print(abs(d) - modulo)

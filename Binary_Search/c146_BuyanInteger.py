# https://atcoder.jp/contests/abc146/tasks/abc146_c

import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a, b, x = MI()
lbnd, ubnd = -1, 1_000_000_000

while abs(ubnd - lbnd) > 1:
  idx = (lbnd + ubnd) // 2
  val = idx + 1
  required = a * val + b * len(str(val))
  if required <= x:
    # compact Good case
    lbnd = idx
  else:
    # compact Bad case
    ubnd = idx

if lbnd == -1:
  print(0)
else:
  print(ubnd)

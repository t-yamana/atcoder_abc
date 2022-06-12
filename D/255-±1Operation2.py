# https://atcoder.jp/contests/abc255/tasks/abc255_d

import sys, bisect
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, q = MI()
arr = sorted(LI())

mn = arr[0]
mx = arr[-1]

sums = [None] * n
under, above = 0, sum(arr)
for i in range(n):
  under = under + arr[i]
  above = above - arr[i]
  sums[i] = (under, above)
total = under

for _ in range(q):
  x = I()

  if x <= mn:
    print(total - x*n)
    continue
  elif mx <= x:
    print(x*n - total)
    continue

  idx = bisect.bisect_left(arr, x)
  left = x*idx - sums[idx-1][0]
  right = sums[idx-1][1] - x*(n-idx)
  print(left + right)

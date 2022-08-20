# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_a

import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

n, x = MI()
arr = LI()

lbnd, ubnd = 0, len(arr)  # ubnd 最後尾外しているのに注意

while abs(ubnd - lbnd) > 1:
  idx = (lbnd+ubnd) // 2
  if arr[idx] < x:
    # 条件合致していないので外す
    lbnd = idx
  else:
    # 条件合致見つかっているがより絞る
    ubnd = idx

if ubnd == len(arr):
  # 一度も条件合致が見つかっていない
  print(-1)
else:
  if arr[lbnd] < x:
    # [..., x-1, x, ...]
    print(ubnd)
  else:
    print(lbnd)

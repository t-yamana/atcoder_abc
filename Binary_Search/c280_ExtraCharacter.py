# https://atcoder.jp/contests/abc280/tasks/abc280_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

org = S()
dum = S()

lbnd, ubnd = 0, len(dum)  # ubnd は外す

while abs(ubnd - lbnd) > 1:
  idx = (lbnd + ubnd) // 2

  check1 = org[lbnd:idx]
  check2 = dum[lbnd:idx]
  # 一文字で比較するとたまたま一致しているケースで誤判断する

  if check1 == check2:
    lbnd = idx  # 変更箇所後ろにある
  else:
    ubnd = idx  # 変更箇所前にある

if ubnd == len(dum):
  print(len(dum))  # ubnd に変更がない -> 最後一文字が追加
elif org[lbnd:lbnd+1] == dum[lbnd:lbnd+1]:
  print(ubnd+1)
else:
  print(lbnd+1)  # 1_based

# https://atcoder.jp/contests/abc179/tasks/abc179_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
cnt = 0

for a in range(1, n):

  # 以下のコードは冗長
  # for b in range(1, (n-1)//a + 1):
  #   if n >= a * b:
  #     cnt += 1

  # この一行に集約できる
  cnt += (n-1)//a

print(cnt)

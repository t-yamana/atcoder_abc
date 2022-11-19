# https://atcoder.jp/contests/abc278/tasks/abc278_c

from sys import stdin
readline = stdin.readline
def I(): return int(readline().rstrip())
def MI(): return map(int, readline().rstrip().split())
def LI(): return list(map(int, readline().rstrip().split()))
def S(): return readline().rstrip()
def LS(): return list(readline().rstrip().split())

N, Q = MI()

follows = set()

for _ in range(Q):
  T, A, B = MI()
  if T==1:
    follows.add((A,B))
  elif T==2:
    follows.discard((A,B))
  else:
    if ((A,B) in follows and (B,A) in follows):
      print("Yes")
    else:
      print("No")

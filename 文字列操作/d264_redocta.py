# https://atcoder.jp/contests/abc264/tasks/abc264_d

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

mapper = {
  'a': 0, 't': 1, 'c': 2,
  'o': 3, 'd': 4, 'e': 5, 'r': 6
}
txt = [mapper[c] for c in S()]
cost = 0
l_fixed, r_fixed = 0, 0
for idx, v in enumerate([0,6,1,5,2,4,3]):
  if idx%2 == 0:
    move = txt.index(v) - l_fixed
    l_fixed += 1
  else:
    move = (6 - r_fixed) - txt.index(v)
    r_fixed += 1
  cost = cost + move
  txt.remove(v)
  txt.insert(v, 'X')

print(cost)

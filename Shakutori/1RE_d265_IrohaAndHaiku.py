# https://atcoder.jp/contests/abc265/tasks/abc265_d

# 尺取り法実装が難しい、コチラの方が圧倒的に実装がラクな解法▼
# https://qiita.com/u2dayo/items/51f4780e7da7aee73877#%E8%80%83%E5%AF%9F-3

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
import itertools

N, P, Q, R = MI()
_arr = LI()
arr = [0] + list(itertools.accumulate(_arr))

def betsum(x: int, y: int) -> int:
  return arr[y]-arr[x]

# yを進めるため、この関数はこれで 22AC できる
def nextYZ(y,z) -> tuple:
  if y>=z: print('dummy')
  global Q
  total = betsum(y,z)
  if total == Q or z-y == 1:
    return (y+1, z+1)
  else:
    return (y, z)  # yは進める必要なし

x, y, z, w = 0, 1, 2, 3
while True:
  while betsum(y,z) < Q and z < len(arr)-2:
    z += 1
  while betsum(y,z) > Q and 1 < z-y:
    y += 1

  if betsum(y,z) != Q:
    if z == len(arr)-2:
      print('No')
      exit()
    else:
      y,z = nextYZ(y,z)
      continue

  w = max(w, z+1)  # z++ へ

  while betsum(x,y) > P and 1 < y-x:
    x += 1
  assert(x<y)  # 22REの原因ではない
  if betsum(x,y) != P:
    # print(x, y, z, w, "->", betsum(x,y), betsum(y,z), betsum(z,w))
    y,z = nextYZ(y,z)
    continue

  while betsum(z,w) < R and w < len(arr)-1:
    w += 1
  if betsum(z,w) != R:
    # print(x, y, z, w, "->", betsum(x,y), betsum(y,z), betsum(z,w))
    y,z = nextYZ(y,z)
    continue

  # print(x, y, z, w, "->", betsum(x,y), betsum(y,z), betsum(z,w))
  print('Yes')
  exit()

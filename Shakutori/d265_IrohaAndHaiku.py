# https://atcoder.jp/contests/abc265/tasks/abc265_d

# 尺取り法以外の別解
# https://qiita.com/u2dayo/items/51f4780e7da7aee73877#%E8%80%83%E5%AF%9F-3

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, P, Q, R = MI()
arr = LI()

y, z, w = 0, 0, 0
s0, s1, s2 = 0, 0, 0
ok = False

for x in range(N):
  while y < N and s0 < P:
    s0 += arr[y]
    s1 -= arr[y]  # 先に引くと一石二鳥
    y += 1
  while z < N and s1 < Q:
    s1 += arr[z]
    s2 -= arr[z]
    z += 1
  while w < N and s2 < R:
    s2 += arr[w]
    w += 1
  # print(x,y,z,w)
  if s0==P and s1==Q and s2==R:
    ok = True
    break
  s0 -= arr[x]

print('Yes' if ok else 'No')

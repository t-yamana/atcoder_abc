# https://atcoder.jp/contests/past202005-open/tasks/past202005_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

a, r, n = MI()
limit = 1_000_000_000

if r == 1:
  print(a)
  exit()

# r=2 -> n:31, ar^(n-1): 1_073_741_824 * a
# どんな a でもループ計算 31 で終わる(r=1 でさえなければ)
for _ in range(n-1):
  a = a * r
  if a > limit:
    print('large')
    exit()

print(a)

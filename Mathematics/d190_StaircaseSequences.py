# https://atcoder.jp/contests/abc190/tasks/abc190_d

import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
cnt = 0
i = 1
while i*i <= 2*N:  # 約数全探索: O[N^1/2]
  if 2*N % i == 0:
    # 2N = n*(2a+n-1) を満たす n,a の組数を調べる
    n = i
    m = 2*N // i  # m = 2a+n-1 とする
    # ★ m-n == 2a-1 で成立
    if n%2 != m%2:
      # N=12 => (a,n): (12,1),(3,3)
      # a = (m-n+1) // 2
      # print(a, n)
      cnt += 2  # n <=> m の時
  i += 1

print(cnt)

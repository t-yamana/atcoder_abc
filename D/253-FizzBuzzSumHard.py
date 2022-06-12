# https://atcoder.jp/contests/abc253/tasks/abc253_d

import sys
from math import gcd  # greatest common divisor
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

# ACしない(小数にすると計算機の性質上誤差が生じる)
def lcm1(a, b): return a * b / gcd(a, b)
# ACする
def lcm2(a, b): return a * b // gcd(a, b)

# ACしない(小数にすると計算機の性質上誤差が生じる)
def sum_arr1(n): return n * (n+1) / 2
# ACする
def sum_arr2(n): return n * (n+1) // 2

n, a, b = MI()
ab = lcm2(a, b)

ans2 = sum_arr2(n)
ans2 -= a * sum_arr2(n//a)
ans2 -= b * sum_arr2(n//b)
ans2 += ab * sum_arr2(n//ab)

print(int(ans2))

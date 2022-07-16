# https://atcoder.jp/contests/arc107/tasks/arc107_a

import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())

a, b, c = MI()
limit = 998_244_353

def sum_x(n: int) -> int:
  _n = n % limit
  sum_x = _n * (_n+1) // 2
  sum_x = sum_x % limit
  return sum_x

sum_a = sum_x(a)
sum_b = sum_x(b)
sum_c = sum_x(c)

ans = (sum_a * sum_b * sum_c) % limit
print(ans)

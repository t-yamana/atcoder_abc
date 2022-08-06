# https://atcoder.jp/contests/arc098/tasks/arc098_a

import sys
def I(): return int(sys.stdin.readline().rstrip())
def S(): return sys.stdin.readline().rstrip()

n = I()
s = S()

# コストの累積
arr_w = [None] * len(s)  # from Right
arr_w[0] = 1 if s[0] == 'W' else 0

arr_e = [None] * len(s)  # from Left
arr_e[-1] = 1 if s[-1] == 'E' else 0

for i in range(1, len(s)):
  arr_w[i] = arr_w[i-1] + (1 if s[i] == 'W' else 0)

for i in reversed(range(0, len(s)-1)):  # リストの逆向き操作
  arr_e[i] = arr_e[i+1] + (1 if s[i] == 'E' else 0)

cost = float('inf')
for i in range(len(s)):
  if i == 0:
    cost = min(cost, arr_e[i+1])
  elif i == len(s)-1:
    cost = min(cost, arr_w[i-1])
  else:
    cost = min(cost, arr_w[i-1]+arr_e[i+1])

print(cost)

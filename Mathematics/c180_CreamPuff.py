# https://atcoder.jp/contests/abc180/tasks/abc180_c

import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()
arr1, arr2 = [], []

i = 1
while i*i <= N:  # 約数全探索 O[N^1/2]
  if N % i == 0:
    arr1.append(i)
    arr2.append(N//i)
  i += 1

# ★ N=16 => [...4], [...4]
if arr1[-1] == arr2[-1]:
  arr2.pop(-1)

for a in arr1:
  print(a)
for a in arr2[::-1]:
  print(a)

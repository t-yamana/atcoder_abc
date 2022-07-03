# https://atcoder.jp/contests/abc254/tasks/abc254_b

from copy import deepcopy

num = int(input())
tmp = []
for i in range(num):
  tmp.append(1)
  print(' '.join([str(n) for n in tmp]))
  new_tmp = deepcopy(tmp)
  for j in range(1, i+1):
    new_tmp[j] = tmp[j-1] + tmp[j]
  tmp = new_tmp

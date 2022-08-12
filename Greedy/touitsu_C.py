# https://atcoder.jp/contests/nikkei2019-qual/tasks/nikkei2019_qual_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

n = I()
dishes = [tuple(LI()) for _ in range(n)]
dishes.sort(key= lambda d: d[0]+d[1], reverse=True)

tk = 0
ao = 0
for i in range(n):
  if i%2 == 0:
    tk += dishes[i][0]
  else:
    ao += dishes[i][1]

print (tk-ao)

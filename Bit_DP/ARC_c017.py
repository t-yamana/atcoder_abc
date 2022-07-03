# https://atcoder.jp/contests/arc017/tasks/arc017_3
# 半分全列挙(Bit)

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, x = MI()
weights = [I() for _ in range(n)]

wei1 = weights[:n//2]
wei2 = weights[n//2:]

def subTotalDict(weights: list) -> dict:
  sub_total1 = dict()
  for i in range(1<<len(weights)):
    total = 0
    for sft in range(len(weights)):
      if i == i | (1<<sft):
        total += weights[sft]
    sub_total1.setdefault(total, 0)
    sub_total1[total] += 1
  return sub_total1

wei1_combs = subTotalDict(wei1)
wei2_combs = subTotalDict(wei2)

grand_total = 0
for k,v in wei1_combs.items():
  if k<=x:
    grand_total += v * wei2_combs.get(x-k, 0)
print(grand_total)

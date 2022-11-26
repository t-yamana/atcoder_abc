# https://atcoder.jp/contests/abc279/tasks/abc279_c

import sys

def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

H, W = MI()
# Multi-Set があれば一発かも

shape_S = [[None] * H for _ in range(W)]
for r in range(H):
  for idx, v in enumerate(S()):
    shape_S[idx][r] = '1' if v == '#' else '0'

bit_S = [None] * W
total_S = 0
index = 0
for bits in shape_S:
  bit_S[index] = int("".join(bits), 2)
  total_S += bit_S[index]
  index += 1

shape_T = [[None] * H for _ in range(W)]
for r in range(H):
  for idx, v in enumerate(S()):
    shape_T[idx][r] = '1' if v == '#' else '0'

bit_T = [None] * W
total_T = 0
index = 0
for bits in shape_T:
  bit_T[index] = int("".join(bits), 2)  # ['0','1','1'] => 0b011
  total_T += bit_T[index]
  index += 1

# これだけだと カブりが追跡できない
# check1 = frozenset(bit_T) == frozenset(bit_S)
# カブりも含めて区別されている?
# check2 = total_S == total_T

check = sorted(bit_T) == sorted(bit_S)
print("Yes" if check else "No")

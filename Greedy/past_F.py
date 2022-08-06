# https://atcoder.jp/contests/past202004-open/tasks/past202004_f

import sys, heapq
def I(): return int(sys.stdin.readline().rstrip())
def TI(): return tuple(map(int,sys.stdin.readline().rstrip().split()))

n = I()
tups = [None] * n

for i in range(n):
  tups[i] = TI()
  # ソートせずここで日別のタスクリストを作る方法もある
tups.sort(key = lambda x: x[0])

choices = []
score = 0
i = 0  # tups のポインターとして利用することで一周で済む
for day in range(1, n+1):
  while i < len(tups) and tups[i][0] <= day:
    heapq.heappush(choices, -1 * tups[i][1])
    i += 1
  score += heapq.heappop(choices) * -1
  print(score)

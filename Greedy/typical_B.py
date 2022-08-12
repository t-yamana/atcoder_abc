# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_b
# 区間スケジューリング問題

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))

n = I()
tasks = [tuple(LI()) for _ in range(n)]
tasks.sort(key= lambda t: t[1])  # 終了時でソート

lock_end = 0
cnt = 0
for t in tasks:
  if t[0] > lock_end:
    cnt += 1
    lock_end = t[1]
print(cnt)

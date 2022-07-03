# https://atcoder.jp/contests/typical-algorithm/tasks/typical_algorithm_c

import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
costs = [LI() for _ in range(n)]

dp = [[None] * n for _ in range(1<<n)]
dp[0b0][0] = 0

for i in range(1<<n):
  for sft in range(1, n):  # 往き先
    if i == i | (1<<sft):
      continue  # 訪問済み

    for idx, cost in enumerate(dp[i]):  # 出発元
      if cost is not None:
        new_cost = cost + costs[idx][sft]
        dest = dp[i|(1<<sft)][sft]
        if dest:
          dp[i|(1<<sft)][sft] = min(dest, new_cost)
        else:
          dp[i|(1<<sft)][sft] = new_cost

for idx, cost in enumerate(dp[-2]):  # 0b1110
  if cost is None:
    continue
  new_cost = cost + costs[idx][0]
  goal = dp[-1][0]  # 0b1111
  if goal:
    dp[-1][0]= min(goal, new_cost)
  else:
    dp[-1][0] = new_cost
print(dp[-1][0])

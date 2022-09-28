# https://atcoder.jp/contests/abc270/tasks/abc270_c

import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
sys.setrecursionlimit(1_000_000)

N, X, Y = MI()
diag = [[] for _ in range(N+1)]
seen = [False] * (N+1)
for _ in range(N-1):
  U, V = MI()
  diag[U].append(V)
  diag[V].append(U)

def dfs(now: int, goal: int) -> None:
  seen[now] = True
  for next in diag[now]:
    if next == goal:  # 終了条件
      path.append(goal)
      print(' '.join(map(str, path)))
      exit()
    elif seen[next] is not True:
      path.append(next)
      dfs(next, goal)  # pypyは再帰が遅い
      path.pop(-1)

path = [X]
dfs(X, Y)

# https://atcoder.jp/contests/abc269/tasks/abc269_d

import sys
def I(): return int(sys.stdin.readline().rstrip())
def TI(): return tuple(map(int,sys.stdin.readline().rstrip().split()))

sys.setrecursionlimit(1_000_000)

N = I()
coos = [TI() for _ in range(N)]

def dfs(t: tuple) -> None:
  x, y = t[0], t[1]

  global g_path
  g_path.append((x,y))

  for i, j in [(-1,-1), (-1,0), (0,-1), (0,1), (1,0), (1,1)]:
    if (x+i, y+j) in coos and (x+i, y+j) not in g_path:
      dfs((x+i, y+j))

  global done
  done.extend(g_path)

done = []
score = 0
for coo in coos:
  if coo not in done:
    score += 1
    g_path = []  # 経路座標リストをリフレッシュ
    dfs(coo)
print(score)

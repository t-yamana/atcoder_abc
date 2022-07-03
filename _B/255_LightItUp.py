import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, k = MI()
lights = [idx - 1 for idx in LI()]

coos = [None] * n
for idx in range(n):
  x, y = MI()
  coos[idx] = (x, y)

dists = []
for idx in range(n):
  if idx in lights:
    continue
  else:
    x, y = coos[idx]
    min_dist = float('inf')
    for i in lights:
      lx, ly = coos[i]
      min_dist = min(min_dist, pow(pow(x-lx, 2)+pow(y-ly, 2), 0.5))
    dists.append(min_dist)

max_dist = -1
for dist in dists:
  max_dist = max(max_dist, dist)
print(max_dist)

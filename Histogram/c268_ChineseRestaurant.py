
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n = I()
dishes = LI()

di = []
for idx, i in enumerate(dishes):

  # TLE:
  # delta = dishes.index(idx) - i
  delta = i - idx

  di.append(delta if delta >= 0 else n+delta)
print(di)

hist = dict(zip(list(range(n)), [0]*n))
for v in di:
  hist[v] += 1

hist.setdefault(n, 0)
hist[n] = hist[0]

pt = hist[0]+hist[1]+hist[2]
maxpt = hist[0]+hist[1]+hist[2]

for i in range(n-1):
  pt = hist[i]+hist[i+1]+hist[i+2]  # hist[n]まで
  maxpt = max(pt, maxpt)

print(maxpt)

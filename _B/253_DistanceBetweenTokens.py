import sys


def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

h, w = MI()
pts = []
for i in range(h):
  txt = input()
  for _ in range(2):
    try:
      idx = txt.index('o')
      txt = txt.replace('o', '-', 1)
      pts.append((i, idx))
    except ValueError:
      break

delta_h = abs(pts[0][0]-pts[1][0])
delta_w = abs(pts[0][1]-pts[1][1])
print(delta_h + delta_w)

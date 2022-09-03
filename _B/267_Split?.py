
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

pos = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
pins = S()

for idx, c in enumerate(pins):
  if c == '0':
    pos[idx] = -1

left_rows = []
for i in range(7):
  if i in pos:
    left_rows.append(i)

last = None
for r in left_rows:
  if last is not None and abs(r - last) > 1:
    if pos[0] == -1:
      print('Yes')
      exit()
  last = r

print('No')

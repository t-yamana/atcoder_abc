
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, m = MI()
arr = LI()

val = 0
simple = 0

for i in range(0, m):
  simple += arr[i]
  val += (i+1) * arr[i]

big = val

for i in range(0, n-m):
  val = val - simple + m * arr[i+m]
  simple = simple - arr[i] + arr[i+m]

  big = max(big, val)

print(big)


import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

n, m = MI()
arr = LI()

dp = [[None] * n for _ in range(m+1)]  # m*(n-1)
dp[0][0] = 0
dp[1][0] = arr[0]

for i in range(1, m+1):
  for j in range(i-1, n):
    if i==1 and j==0:
      continue
    else:
      choice1 = i * arr[j] + (dp[i-1][j-1] if dp[i-1][j-1] else 0)
      choice2 = dp[i][j-1] if dp[i][j-1] else -1 * float('inf')
      dp[i][j] = max(choice1, choice2)

print(dp[m][n-1])

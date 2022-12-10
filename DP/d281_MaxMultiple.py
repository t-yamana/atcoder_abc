
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N, K, D = MI()
arr = LI()

dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
  for j in range(K+1):
    for k in range(D):
      base = dp[i][j][k]
      if base == -1:
        continue

      # arr[i] 選ばない場合
      dp[i+1][j][k] = max(base, dp[i+1][j][k])

      # arr[i] 選ぶ場合
      if j != K:  # 選択スロットに空きがある
        new = base + arr[i]
        old = dp[i+1][j+1][(k+arr[i]) % D]
        dp[i+1][j+1][(k+arr[i]) % D] = max(old, new)

print(dp[N][K][0])

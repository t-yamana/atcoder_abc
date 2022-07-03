# https://atcoder.jp/contests/abc242/tasks/abc242_c

if __name__ == "__main__":
  md = 998244353
  n = int(input())
  dp = [[0] * 10 for _ in range(n+1)]

  for c in range(1, 10):
    dp[1][c] = 1

  for r in range(2, n+1):
    for c in range(1, 10):
      c_search = [c-1, c, c+1]

      if c == 1:
        c_search = c_search[1:]
      elif c == 9:
        c_search = c_search[:2]

      cnt = 0
      for s_c in c_search:
        cnt += dp[r-1][s_c]
      dp[r][c] = cnt % md

  print(sum(dp[n]) % md)

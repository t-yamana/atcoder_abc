
n = int(input())
pool = [0] + [None] * (2*n+1)

while True:
  ans = pool.index(None)
  pool[ans] = ans
  print(ans, flush=True)

  reply = int(input())
  pool[reply] = reply
  if reply == 0:
    break

import sys


def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

N = I()
arr = LI()

# 単純増加部分を明らかにする
last_idx = len(arr)-1
last_v = arr[-1]

constant_plus = True
while last_idx > 0:
  if arr[last_idx] > last_v:
    break
  last_v = arr[last_idx]
  last_idx -= 1

# 使える数のリスト
usable = sorted(arr[last_idx:], reverse=True)

# 必ず利用できる小さい数が入っている
repl = list(filter(lambda n: n < arr[last_idx], usable))[0]

ans = arr[:last_idx]
ans.append(repl)
ans.extend(list(filter(lambda n: n != repl, usable)))
print(*ans)

pass

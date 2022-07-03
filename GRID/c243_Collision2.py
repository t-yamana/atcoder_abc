# https://atcoder.jp/contests/abc243/tasks/abc243_c

n = int(input())
mtx = [None] * n
for i in range(n):
  mtx[i] = list(map(int, input().split()))

pair = dict()
for i, c in enumerate(input()):
  pt = mtx[i]
  # y値: { Rへ向かう最小のx値, Lへ向かう最大のx値 } の辞書を作成する
  xs = pair.setdefault(pt[1], [None, None])

  # 初回入力時
  if xs[0] is None and xs[1] is None:
    xs["RL".index(c)] = pt[0]  # x値
    pair[pt[1]] = xs
    continue

  if c=="L":
    # Lへ向かう最大のx値
    xs[1] = max(xs[1], pt[0]) if xs[1] is not None else pt[0]
    pair[pt[1]] = xs
  elif c == "R":
    # Rへ向かう最小のx値
    xs[0] = min(xs[0], pt[0]) if xs[0] is not None else pt[0]
    pair[pt[1]] = xs

for p in pair.values():
  # 衝突判定
  if p[0] is not None and p[1] is not None and p[0]<p[1]:
    print("Yes")
    exit()

print("No")  # 衝突しない

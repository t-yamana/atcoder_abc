# https://atcoder.jp/contests/abc249/tasks/abc249_c

def k_len_count(text: str, k: int) -> int:
  hist = {}
  for c in text:
    hist.setdefault(c, 0)
    hist[c] += 1
  cnt = 0
  for v in hist.values():
    if v == k:
      cnt += 1
  return cnt


n, k = map(int, input().split())
txts = [None] * n
for i in range(n):
  txts[i] = input()

max_ans = 0
for i in range(1 << n):
  txt = ""
  for j in range(n):
    if i & (1 << j):
      txt += txts[j]
  max_ans = max(max_ans, k_len_count(txt, k))

print(max_ans)

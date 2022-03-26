# https://atcoder.jp/contests/abc245/tasks/abc245_c

n, k = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))

hands = [arr_a[0], arr_b[0]]
for i in range(1, n):
  if len(hands) == 0: break
  new_hands = set()
  for h in hands:
    if abs(arr_a[i] - h) <= k:
      new_hands.add(arr_a[i])
    if abs(arr_b[i] - h) <= k:
      new_hands.add(arr_b[i])
  hands = list(new_hands)

print("Yes") if len(hands) > 0 else print("No")

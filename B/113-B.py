
n = int(input())
t, a = (int(a) for a in input().split())
h_arr = [int(a) for a in input().split()]

diff = float('inf')
ans = None
for i, h in enumerate(h_arr, 1):
    tmp_diff = abs(a - (t - 0.006 * h))
    if tmp_diff < diff:
        ans = i
        diff = tmp_diff

print(ans)

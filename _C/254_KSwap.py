# https://atcoder.jp/contests/abc254/tasks/abc254_c

if __name__ == "__main__":
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))

  sp_arr = []
  for i in range(k):
    sp_arr.append(arr[i%k::k])

  for ar in sp_arr:
    ar.sort()

  # print(sp_arr)
  mx = len(sp_arr[0])  # 最長

  sim_sorted = []
  for i in range(mx):
    for a in sp_arr:
      if i < len(a):
        sim_sorted.append(a[i])

  # print(sim_sorted)
  print('Yes' if sim_sorted == sorted(arr) else 'No')

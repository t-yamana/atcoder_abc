
arr = [int(s) for s in input().split()]
arr = sorted(arr)
delta = arr[1] - arr[0]
print('Yes' if arr[2] - arr[1] == delta else 'No')

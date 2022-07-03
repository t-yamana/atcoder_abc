
n, k = map(int, input().split())

friend_point = []
for i in range(n):
    friend_point.append(tuple(int(a) for a in input().split()))

friend_point.sort(key=lambda x: x[0])

idx = 0
for i in range(n):
    if friend_point[i][0] <= k:
        k += friend_point[i][1]
print(k)

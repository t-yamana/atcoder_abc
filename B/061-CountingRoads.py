
if __name__ == '__main__':
    n, m = map(int, input().split())  # アンパック
    cities = [0] * n

    for i in range(m):
        road = list(map(int, input().split()))  # 1 ~ n
        cities[road[0] - 1] += 1  # 0 ~ n-1
        cities[road[1] - 1] += 1  # 0 ~ n-1

    for cnt in cities:
        print(cnt)

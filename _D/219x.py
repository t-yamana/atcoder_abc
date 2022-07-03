
if __name__ == '__main__':
    num = int(input())
    wants = list(map(int, input().split()))

    vents = [None] * num
    for i in range(num):
        a, b = map(int, input().split())  # unpack
        vents[i] = tuple([a, b, a+b])

    vents = sorted(vents, key=lambda tup: tup[2], reverse=True)
    print(vents)

    sums = wants
    for v in vents:
        sums = [sums[0] - v[0], sums[1] - v[1]]
    if sums[0] > 0 or sums[1] > 0:
        print(-1)
        exit()

    cnt = 0
    for v in vents:
        wants = [wants[0] - v[0], wants[1] - v[1]]
        print(wants)
        cnt += 1
        if wants[0] <= 0 and wants[1] <= 0:
            break
    print(cnt)

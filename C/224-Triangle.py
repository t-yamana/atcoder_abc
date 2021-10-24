
if __name__ == '__main__':
    n = int(input())

    coos = [tuple(map(int, input().split())) for _ in range(n)]

    # itertools.combinations なんか使用しなくていい
    # 3重for文となにも変わらない
    # cmbs = combinations(range(n), 3)

    # math.factorial なんて使わなくていい
    count = n*(n-1)*(n-2)//6

    for i in range(n):
        p1 = coos[i]
        for j in range(i+1, n):
            p2 = coos[j]
            x1 = (p2[0]-p1[0])
            y1 = (p2[1]-p1[1])
            for k in range(j+1, n):
                p3 = coos[k]
                calc = x1 * (p3[1]-p1[1]) - (p3[0]-p1[0]) * y1
                # ココで全てを計算すると TLE
                # calc=(p2[0]-p1[0])*(p3[1]-p1[1])-(p3[0]-p1[0])*(p2[1]-p1[1])
                if calc == 0:
                    count -= 1
    print(count)

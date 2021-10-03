
if __name__ == '__main__':
    n = int(input())

    sched = [None] * n
    for i in range(n):
        sched[i] = tuple(map(int, input().split()))

    t = 0
    x, y = 0, 0

    for plan in sched:
        if (plan[0] - t) < abs(plan[1] - x) + abs(plan[2] - y):
            print('No')
            exit()

        cood = plan[1] + plan[2]
        if cood % 2 == 0:
            if plan[0] % 2 == 1:
                print('No')
                exit()
        else:
            if plan[0] % 2 == 0:
                print('No')
                exit()

        t, x, y = plan[0], plan[1], plan[2]

    print('Yes')

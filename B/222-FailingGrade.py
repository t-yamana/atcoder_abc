
if __name__ == '__main__':
    n, p = map(int, input().split())
    scores = list(map(int, input().split()))
    fails = 0
    for s in scores:
        if s < p:
            fails += 1
    print(fails)

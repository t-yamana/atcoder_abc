
if __name__ == '__main__':
    n = int(input())
    dict = {}
    for i in range(1, n+1):
        nxt = int(input())
        dict[i] = nxt

    state = 1
    trail = set()
    while True:
        nxt = dict[state]

        if nxt == 2:
            trail.add(nxt)
            break
        if nxt in trail:  # ループに入ってしまった
            print(-1)
            exit()
        else:
            trail.add(nxt)
            state = nxt

    print(len(trail))

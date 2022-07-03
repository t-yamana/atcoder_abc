
if __name__ == '__main__':
    n = int(input())

    connects = {}

    for i in range(n-1):
        s, g = map(int, input().split())
        connects.setdefault(s, [])
        connects[s].append(g)

        connects.setdefault(g, [])
        connects[g].append(s)

    is_star = False
    for arr in connects.values():
        if len(arr) == n-1:
            is_star = True

    print('Yes') if is_star else print('No')


if __name__ == '__main__':
    org_alp = 'abcdefghijklmnopqrstuvwxyz'
    nxt_alp = input()

    next_dict = {}
    for i in range(26):
        next_dict[nxt_alp[i]] = org_alp[i]

    reverse_dict = {}
    for i in range(26):
        reverse_dict[org_alp[i]] = nxt_alp[i]

    cnt = int(input())
    mans = [None] * cnt
    for i in range(cnt):
        org_name = input()
        nxt_name = ''
        for c in org_name:
            nxt_name += next_dict[c]
        mans[i] = nxt_name

    arr = sorted(mans, reverse=False)
    for a in arr:
        real_name = ''
        for c in a:
            real_name += reverse_dict[c]
        print(real_name)

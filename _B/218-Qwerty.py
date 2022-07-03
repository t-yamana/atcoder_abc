
if __name__ == '__main__':
    order = list(map(int, input().split()))
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    ans = ''
    for i in range(26):
        ans += alphabets[order[i] - 1]
    print(ans)

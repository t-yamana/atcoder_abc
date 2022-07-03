
if __name__ == '__main__':
    n, k = map(int, input().split())
    pat = k * pow(k-1, n-1)
    print(pat)

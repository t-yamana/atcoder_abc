
if __name__ == '__main__':
    a, b, c, d = map(int, input().split())
    print(max(0, min(b, d) - max(a, c)))

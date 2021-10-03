
if __name__ == '__main__':
    a, b, c = map(int, input().split())
    for num in range(a, b+1):
        if num % c == 0:
            print(num)
            exit()
    print(-1)
    exit()

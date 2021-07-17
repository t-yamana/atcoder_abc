
if __name__ == '__main__':
    n, a, x, y = map(int, input().split())
    if n > a:
        # with bonus cabbage
        print(a*x + (n-a)*y)
    else:
        # without bonus cabbage
        print(n*x)

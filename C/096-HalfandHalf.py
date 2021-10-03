
if __name__ == '__main__':
    a, b, c, x, y = map(int, input().split())
    price = a*x + b*y

    # 組み替えた方が安いなら
    suppress = a+b - c*2
    if suppress > 0:
        times = min(x, y)
        x -= times
        y -= times
        assert(x == 0 or y == 0)
        price -= suppress * times

    # さらに、Cを2枚買う方が個別で買うより安いなら
    if c*2 < a:
        suppress = a - c*2
        price -= suppress * x
    if c*2 < b:
        suppress = b - c*2
        price -= suppress * y

    print(price)

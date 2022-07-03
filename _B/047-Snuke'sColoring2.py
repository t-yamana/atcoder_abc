
if __name__ == '__main__':
    w, h, n = map(int, input().split())  # アンパック
    x_max, y_max = w, h
    x_min, y_min = 0, 0

    for i in range(n):
        x, y, direct = map(int, input().split())
        if direct == 1:
            if x_min < x:
                x_min = x
        elif direct == 2:
            if x < x_max:
                x_max = x
        elif direct == 3:
            if y_min < y:
                y_min = y
        elif direct == 4:
            if y < y_max:
                y_max = y

    print(x_min, x_max)
    print(y_min, y_max)

    print(x_max - x_min)
    print(y_max - y_min)
    area = (y_max - y_min) * (x_max - x_min)
    print(area)

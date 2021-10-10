
if __name__ == '__main__':
    a, b, c = map(int, input().split())

    excess = set()
    mul = 1
    calcable = True

    while True:
        val = (a * mul) % b
        if val == c:
            calcable = True
            break
        # 余剰がループ二週目に入ったら終了する
        elif val in excess:
            calcable = False
            break
        else:
            excess.add(val)
        mul += 1

    print('YES' if calcable else 'NO')

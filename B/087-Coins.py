from typing import Tuple


def fifty_check(c: int, x: int) -> Tuple[int, int]:
    '''確定分の50円一枚を事前に見込む'''
    if x % 100 == 50:
        if c > 0:
            x -= 50
            c -= 1
        else:
            raise ValueError
    return (c, x)


def counting(a, b, c, org_x) -> int:
    num_pats = 0
    for i in range(a+1):
        if 500 * i > org_x:
            break  # 打ち切り
        for j in range(b+1):
            if 500 * i + 100 * j > org_x:
                break  # 打ち切り
            for k in range(c+1):
                calc_x = 500 * i + 100 * j + 50 * k
                if calc_x > org_x:
                    break  # 打ち切り
                elif calc_x == org_x:
                    num_pats += 1
                    # print(i, j, k)
                    break
                else:
                    continue
    return num_pats


def count_patterns(a, b, c, x) -> None:
    try:
        c, x = fifty_check(c, x)
    except ValueError:
        print(0)
        return
    ans = counting(a, b, c, x)
    print(ans)


a = int(input())
b = int(input())
c = int(input())
x = int(input())
count_patterns(a, b, c, x)

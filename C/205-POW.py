

def pow_compare(a: int, b: int, pow: int) -> str:
    is_bigger_right = False  # '>' と仮置く

    # pow が 0
    if pow == 0:
        return '='
    if a == b:
        return '='

    # pow が 偶数・奇数
    if pow % 2 == 1:
        if a < b:
            is_bigger_right = True
    else:
        if abs(a) == abs(b):
            return '='
        if abs(a) < abs(b):
            is_bigger_right = True

    if pow < 0:
        is_bigger_right = not(is_bigger_right)

    return '<' if is_bigger_right else '>'


if __name__ == '__main__':
    a, b, c = map(int, input().split())
    print(pow_compare(a, b, c))

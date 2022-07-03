

def over_redball(start_b: int, b: int, r: int, xross: int) -> int:
    # 既に条件達成
    if start_b == 0:
        return 0

    # b > r でも、xross がデカければチャンスはある

    i = 0
    delta = float('inf')
    while True:
        new_delta = (start_b + i * b) - (xross * r * i)
        if new_delta <= 0:
            return i
        elif delta > new_delta:
            delta = new_delta
        else:
            return -1
        i += 1


start_b, b, r, xross = map(int, input().split())
print(over_redball(start_b, b, r, xross))

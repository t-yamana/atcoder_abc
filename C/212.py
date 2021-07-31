# Min Difference

if __name__ == '__main__':
    n, m = map(int, input().split())
    ls_a = map(int, input().split())
    ls_b = map(int, input().split())

    ls_a = sorted(ls_a)
    ls_b = sorted(ls_b)

    i = j = 0
    minimum = float('inf')

    # Order(n*m) -> Order(max(n*log(n), m*log(m)) らしい
    while i < n and j < m:
        diff = ls_a[i] - ls_b[j]
        minimum = min(minimum, abs(diff))

        if diff > 0:
            j += 1
        elif diff < 0:
            i += 1
        else:
            break  # 一致

    print(minimum)

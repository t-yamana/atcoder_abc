
def sum_alt_adj_cnt(arr, updown: 1) -> int:
    cnt, sum = 0, 0
    for idx in range(len(arr)):
        sum += arr[idx]
        if idx % 2 == 0:
            if sum * updown > 0:
                continue
            else:
                fix = -1 * (sum - updown)
                sum += fix
                cnt += abs(fix)
        else:
            if sum * updown * (-1) > 0:
                continue
            else:
                fix = -1 * (sum + updown)
                sum += fix
                cnt += abs(fix)
    return cnt


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    # +, -, +, -, ...
    cnt1 = sum_alt_adj_cnt(arr, 1)
    # -, +, -, +, ...
    cnt2 = sum_alt_adj_cnt(arr, -1)

    print(min(cnt1, cnt2))


if __name__ == '__main__':
    arr = sorted(list(map(int, input().split())))

    cnt = 0
    while arr[0] != arr[1] or arr[1] != arr[2]:
        mx = max(arr)

        arr.remove(mx)
        inv_arr = list(map(lambda a: mx-a, arr))

        if 0 in inv_arr:
            assert(inv_arr[0] != 0)
            arr[0] += 2
        else:
            arr[0] += 1
            arr[1] += 1

        arr = sorted(arr) + [mx]
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    one_pack = sum(arr)
    loop = x // one_pack
    x = x % one_pack

    sum = 0
    for idx in range(len(arr)):
        sum += arr[idx]
        if sum > x:
            print(len(arr) * loop + (idx+1))
            exit()

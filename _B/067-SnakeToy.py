
if __name__ == '__main__':
    n, k = map(int, input().split())  # アンパック
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse=True)

    s_len = sum(arr[0:k:1])
    print(s_len)

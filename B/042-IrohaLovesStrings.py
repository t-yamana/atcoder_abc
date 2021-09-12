
if __name__ == '__main__':
    n, _ = map(int, input().split())  # アンパック

    arr = [None] * n
    for i in range(n):
        arr[i] = input()

    arr = sorted(arr)
    concat_arr = ''.join(arr)
    print(concat_arr)

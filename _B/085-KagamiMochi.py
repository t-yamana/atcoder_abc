
if __name__ == '__main__':
    n = int(input())

    arr = [None] * n
    for i in range(n):
        arr[i] = int(input())

    arr = list(set(arr))
    print(len(arr))


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr = sorted(arr, reverse=True)

    a_score = sum(arr[::2])
    b_score = sum(arr[1::2])

    print(a_score - b_score)

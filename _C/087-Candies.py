
if __name__ == '__main__':
    n = int(input())

    cells = [[None] * n, [None] * n]

    cells[0] = list(map(int, input().split()))
    cells[1] = list(map(int, input().split()))

    biggest = 0
    for i in range(n):
        total = sum(cells[0][:i+1:]) + sum(cells[1][i::])
        if total > biggest:
            biggest = total

    print(biggest)

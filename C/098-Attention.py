
if __name__ == '__main__':
    n = int(input())
    arr = input()

    forces = arr[1::].count('E')
    min_forces = forces

    for i in range(1, n):
        # 毎回0からポイントを計算するとダメ
        # forces = arr[:i:].count('W') + arr[i::].count('E')

        # 前回の計算結果から差分のみで更新するとOK
        if arr[i] == 'E' and arr[i-1] == 'W':
            forces += 0
        elif arr[i] == 'W' and arr[i-1] == 'W':
            forces += 1
        elif arr[i] == 'E' and arr[i-1] == 'E':
            forces -= 1
        elif arr[i] == 'W' and arr[i-1] == 'E':
            forces -= 0
        min_forces = min(min_forces, forces)

    print(min_forces)



def sum_room_num(n: int, k: int) -> int:
    total = 0
    for i in range(1, n+1):
        for j in range(1, k+1):
            total += 100 * i + j
    return total


n, k = map(int, input().split())
print(sum_room_num(n, k))

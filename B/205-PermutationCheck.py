
from typing import List


def is_sorted_full_arr(n: int, arr: List[int]) -> bool:
    if len(list(set(arr))) != n:
        return False
    if min(arr) != 1:
        return False
    if max(arr) != n:
        return False
    return True


if __name__ == '__main__':
    n = int(input())
    arr = [int(a) for a in input().split()]
    print('Yes') if is_sorted_full_arr(n, arr) else print('No')

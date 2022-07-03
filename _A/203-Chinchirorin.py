
from typing import List


def alone_num(arr: List[int]) -> None:
    if len(set(arr)) == 3:
        print(0)
    else:
        for i in range(2):
            if arr[2] == arr[i]:
                print(arr[1-i])
                return
        print(arr[2])


arr = [int(a) for a in input().split()]
alone_num(arr)

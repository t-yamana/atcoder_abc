
from functools import reduce

arr = [int(s) for s in input()]
answer = reduce(lambda a1, a2: a1+a2, arr, 0)
print(answer)

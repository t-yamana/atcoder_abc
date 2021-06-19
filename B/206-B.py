
import itertools

goal = int(input())
# [0, 1, 3, 6..]
for i, a in enumerate(itertools.accumulate(range(100000))):
    if a >= goal:
        print(i)
        break

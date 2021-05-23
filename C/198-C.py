
import math

r, x, y = map(int, input().split())

step = math.sqrt(x**2 + y**2) / r
if step == 1:
    print(1)
elif math.ceil(step) == 1:
    print(2)
else:
    print(math.ceil(step))

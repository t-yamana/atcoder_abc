
n, x = (int(a) for a in input().split())

minimum_ing = float('inf')
num = 0

for i in range(n):
    ing = int(input())
    if ing < minimum_ing:
        minimum_ing = ing
    if x - ing >= 0:
        x -= ing
    else:
        break
    num = i + 1

print(x // minimum_ing + num)

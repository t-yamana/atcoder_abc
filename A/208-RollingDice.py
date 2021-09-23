
a, b = map(int, input().split())
isOk = 1*a <= b and b <= 6*a
if isOk:
    print('Yes')
else:
    print('No')


def just_fit_47(n: int) -> bool:
    for i in range(0, n//4 + 1, 1):
        for j in range(0, n//7 + 1, 1):
            if 4*i + 7*j == n:
                return True
    return False


n = int(input())
ans = just_fit_47(n)
print('Yes' if ans else 'No')

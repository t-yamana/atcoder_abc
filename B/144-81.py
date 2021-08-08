
def Kuku(n) -> None:
    for i in range(10):
        for j in range(10):
            if i*j == n:
                print('Yes')
                return
    print('No')


if __name__ == '__main__':
    n = int(input())
    Kuku(n)

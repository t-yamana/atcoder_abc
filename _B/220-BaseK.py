
if __name__ == '__main__':
    k = int(input())
    a_str, b_str = input().split()
    a = int(a_str, k)  # k進数->10進数へ
    b = int(b_str, k)
    print(a*b)

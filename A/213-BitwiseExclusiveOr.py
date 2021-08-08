
if __name__ == '__main__':
    a, b = map(int, input().split())
    bi_a = format(a, '08b')
    bi_b = format(b, '08b')

    c = [None] * 8

    for i in range(8):
        if (bi_b[i] == '1'):
            c[i] = 1 - int(bi_a[i])
        else:
            c[i] = int(bi_a[i])

    bi_str = ''.join(map(str, c))
    print(int(bi_str, 2))

# 以下で簡単に出来た
# A^C=B は C=A^B でもある性質
# print(a^b)

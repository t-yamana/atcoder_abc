
def str2int(arr_chars) -> int:
    return int(''.join(arr_chars))


if __name__ == '__main__':
    num_s = input()
    ket = len(num_s)

    combee = []
    for i in range(1, ket):
        combee.append((i, ket-i))
    # print(combee)

    num_s = list(sorted(num_s, reverse=True))
    # print(num_s)

    maxax = 0
    for comb in combee:
        minimum = min(comb[0], comb[1])

        a = [None] * minimum
        b = [None] * minimum

        copied_num_s = num_s.copy()
        for i in range(minimum):
            a[i] = copied_num_s.pop(0)
            b[i] = copied_num_s.pop(0)

        if comb[0] >= comb[1]:
            a += copied_num_s  # リストの結合
        else:
            b += copied_num_s  # リストの結合

        calc = str2int(a) * str2int(b)
        if calc > maxax:
            maxax = calc
        # print(str2int(a), '*', str2int(b), '=', maxax)

    for comb in combee:
        a = [None] * comb[0]

        copied_num_s = num_s.copy()
        for i in range(comb[0]):
            a[i] = copied_num_s.pop(0)

        b = copied_num_s

        calc = str2int(a) * str2int(b)
        if calc > maxax:
            maxax = calc
        # print(str2int(a), '*', str2int(b), '=', maxax)

    print(maxax)

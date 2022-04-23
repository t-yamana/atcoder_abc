# https://atcoder.jp/contests/abc221/tasks/abc221_c

# bit全探索
if __name__ == '__main__':
    N = sorted(input(), reverse=True)
    ans = 0
    for i in range(1 << len(N)):  # 2^9
        lf = 0
        rg = 0
        for j in range(len(N)):
            if i & (1 << j):  # 1, 2, 4, 8...
                print(i, (1 << j), True)
                lf = lf * 10 + int(N[j])
            else:
                # int(3) = ord('3') - ord('0')
                print(i, (1 << j), False)
                rg = rg * 10 + int(N[j])
        print(lf, '*', rg, '=', ans)
        ans = max(ans, lf * rg)

    print(ans)

# next_permutation を使用したらラクになるかも

# https://atcoder.jp/contests/abc199/tasks/abc199_c

if __name__ == '__main__':
    n = int(input())
    txt = list(input())

    sep = len(txt)//2
    flipped = False

    def swap_char(txt, a, b) -> str:
        if flipped:
            if a < sep:
                a += sep
            else:
                a -= sep

            if b < sep:
                b += sep
            else:
                b -= sep

        # str -> List にすることで入れ替えが簡単になる
        txt[a], txt[b] = txt[b], txt[a]

        return txt

    q = int(input())
    for _ in range(q):
        t, a, b = map(int, input().split())
        a, b = map(lambda x: x-1, [a, b])

        if t == 2:
            flipped = not flipped
        else:
            txt = swap_char(txt, a, b)

    if flipped:
        txt = txt[sep:] + txt[:sep]

    print(''.join(txt))


import enum


class Jkn(enum.Enum):
    g = 'G'
    c = 'C'
    p = 'P'


def jkn(i: Jkn, j: Jkn) -> int:
    if i == Jkn.g.value and j == Jkn.c.value:
        pt = 2
    elif i == Jkn.c.value and j == Jkn.p.value:
        pt = 2
    elif i == Jkn.p.value and j == Jkn.g.value:
        pt = 2
    elif i == j:
        pt = 1
    elif i == Jkn.g.value and j == Jkn.p.value:
        pt = 0
    elif i == Jkn.c.value and j == Jkn.g.value:
        pt = 0
    elif i == Jkn.p.value and j == Jkn.c.value:
        pt = 0
    else:
        pt = -1
    assert(pt >= 0)
    return pt


if __name__ == '__main__':
    n, m = map(int, input().split())
    choices = [None] * (2 * n)

    for i in range(n * 2):
        choices[i] = input()

    scores = [None] * 2 * n
    for i in range(2*n):
        scores[i] = [i, 0]

    for r in range(m):
        scores = sorted(scores, key=lambda t: t[0], reverse=False)
        scores = sorted(scores, key=lambda t: t[1], reverse=True)
        for j in range(n):
            a = scores[2*j]
            b = scores[2*j+1]

            a_cho = choices[a[0]][r]
            b_cho = choices[b[0]][r]

            pt = jkn(a_cho, b_cho)

            if pt == 2:
                scores[2*j][1] += 1
            elif pt == 0:
                scores[2*j+1][1] += 1

    scores = sorted(scores, key=lambda t: t[0], reverse=False)
    scores = sorted(scores, key=lambda t: t[1], reverse=True)
    for s in scores:
        print(s[0] + 1)

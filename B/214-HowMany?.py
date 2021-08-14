
def zentan(s, t) -> int:
    pat = 0
    for i in range(s+1):
        for j in range(s-i+1):
            for k in range(s-i-j+1):
                if i * j * k <= t:
                    pat += 1
    return pat


if __name__ == '__main__':
    s, t = map(int, input().split())
    pat = zentan(s, t)
    print(pat)

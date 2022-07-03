
if __name__ == '__main__':
    s = input()
    t = input()
    sub_s = ''

    i = 0

    while i < len(s):
        if s[i] == t[i]:
            sub_s += s[i]
        else:
            tmp = s[i]
            try:
                sub_s = sub_s + s[i+1] + tmp
            except IndexError:
                print('No')
                exit()
            i += 1
        i += 1

    if sub_s == t:
        print('Yes')
    else:
        print('No')

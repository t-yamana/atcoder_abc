
if __name__ == '__main__':
    txt = input()
    chars = set()

    for c in txt:
        chars.add(c)

    var = len(chars)  # variation
    if var == 3:
        print(6)
    elif var == 2:
        print(3)
    else:
        print(1)

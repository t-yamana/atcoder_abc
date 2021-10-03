
if __name__ == '__main__':
    text = input()
    text = text[::-1]

    keywords = [
        'dream'[::-1],
        'erase'[::-1],
        'eraser'[::-1],
        'dreamer'[::-1],
    ]

    flag = True
    while flag:
        if text[0:5] == keywords[0] or text[0:5] == keywords[1]:
            text = text[5::]
            flag = False
        if text[0:6] == keywords[2]:
            text = text[6::]
            flag = False
        if text[0:7] == keywords[3]:
            text = text[7::]
            flag = False
        if flag is True:
            if len(text) == 0:
                print('YES')
                exit()
            else:
                print('NO')
                exit()
        else:
            flag = True

    print(text)

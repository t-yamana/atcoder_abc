
if __name__ == '__main__':
    spell = input()
    dict = {}

    for c in spell:
        value = dict.setdefault(c, 0)  # key が未登録の時 0 で登録後取得

    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for c in alphabets:
        try:
            dict[c]
        except KeyError:
            print(c)
            exit()

    print('None')

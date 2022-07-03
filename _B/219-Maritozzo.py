
if __name__ == '__main__':
    texts = ['', '', '']

    for i in range(3):
        texts[i] = input()

    combines = ''
    choices = input()
    for i in [int(c) for c in choices]:
        combines += texts[i-1]

    print(combines)

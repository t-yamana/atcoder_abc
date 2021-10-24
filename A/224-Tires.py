
if __name__ == '__main__':
    txt = input()
    rvsd = txt[::-1]  # reversed
    flag = rvsd[:2:]
    if flag == 're':
        print('er')
    else:
        print('ist')

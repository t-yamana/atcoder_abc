
if __name__ == '__main__':
    n = int(input())
    s = input()
    idx = s.find('1')
    print('Takahashi') if idx % 2 == 0 else print('Aoki')

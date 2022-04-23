# https://atcoder.jp/contests/abc079/tasks/abc079_c

if __name__ == '__main__':
    nums = list(input())

    # Bit全探索(000 - 111)
    for i in range(1 << 4):
        op1 = '+' if i & (1 << 2) else '-'
        op2 = '+' if i & (1 << 1) else '-'
        op3 = '+' if i & (1) else '-'

        text = f'{nums[0]}{op1}{nums[1]}{op2}{nums[2]}{op3}{nums[3]}'

        if eval(text) == 7:
            print(text, '=7', sep='')
            exit()
